#include "samp.h"

double samp_single_em_1(double x, double y, double step, int type_bound, int max_iter, int size_buf, VSLStreamStatePtr s, double* work)
{
    double h = step, *w = work;
    int ctr_w = size_buf;
    double a = 0.0, f = x*x + y*y + 1.0;
    for (int i = 0; i < max_iter; i++)
    {
        if (ctr_w >= size_buf)
        {
            vdRngGaussian(VSL_RNG_METHOD_GAUSSIAN_ICDF, s, size_buf, w, 0.0, 1.0);
            ctr_w = 0;
        }
        double
            x_new = x + h * x + sqrt(h) * w[ctr_w],
            y_new = y + h * y + sqrt(h) * w[ctr_w+1];
        double f_new = x_new*x_new + y_new*y_new + 1.0;
        if (x_new*x_new + y_new*y_new > 1.0)
        {
            if (type_bound == 0)
                ;
            else if (type_bound == 1)
            {
                double t = solve_inter(x, y, x_new, y_new);
                double
                    x_t_ = (1.0 - t) * x + t * x_new,
                    y_t_ = (1.0 - t) * y * t * y_new;
                double f_t_ = x_t_*x_t_ + y_t_*y_t_ + 1.0;
                a += h * t * (f + f_t_) / 2.0;
            }
            else if (type_bound == 2)
            {
                a += h * (f + f_new) / 2.0;
            }
            break;
        }
        else
        {
            a += h * (f + f_new) / 2.0;
            x = x_new, y = y_new;
            f = f_new;
        }
        ctr_w += 2;
    }
    double v = 1.0/2.0 - a;
    return v;
}

double samp_single_em_2(double x, double y, double step, int type_bound, int max_iter, int size_buf, VSLStreamStatePtr s, double* work)
{
    double h = step, *w = work;
    int ctr_w = size_buf;
    double p;
    for (int i = 0; i < max_iter; i++)
    {
        if (ctr_w >= size_buf)
        {
            vdRngGaussian(VSL_RNG_METHOD_GAUSSIAN_ICDF, s, size_buf, w, 0.0, 1.0);
            ctr_w = 0;
        }
        double
            x_new = x + h * (x - 1.0) + sqrt(h) * w[ctr_w],
            y_new = y - h * (y + 1.0) + sqrt(h) * w[ctr_w+1];
        if (x_new*x_new + y_new*y_new > 1.0)
        {
            double t = solve_inter(x, y, x_new, y_new);
            double
                x_t_ = (1.0 - t) * x + t * x_new,
                y_t_ = (1.0 - t) * y + t * y_new;
            p = x_t_ * y_t_ + x_t_ - y_t_;
            break;
        }
        else
        {
            x = x_new, y = y_new;
        }
        ctr_w += 2;
    }
    double v = p;
    return v;
}

void driver_em_1(double x, double y, double step, int type_bound, int rep, int max_iter, int size_buf, int seed, double* m1, double* m2)
{
    int m = rep;
    double h = step;
    double m1_local = 0.0, m2_local = 0.0;
#pragma omp parallel reduction(+: m1_local, m2_local)
    {
        int rank = omp_get_thread_num();
        VSLStreamStatePtr s;
        vslNewStream(&s, VSL_BRNG_MCG31, seed+rank);
        double* w = malloc(size_buf * sizeof(double));
#pragma omp for schedule(static)
        for (int i = 0; i < m; i++)
        {
            double v = samp_single_em_1(x, y, h, type_bound, max_iter, size_buf, s, w);
            m1_local += v;
            m2_local += v*v;
        }
        free(w);
        vslDeleteStream(&s);
    }
    *m1 = m1_local / m;
    *m2 = m2_local / m;
    return ;
}

void driver_em_2(double x, double y, double step, int type_bound, int rep, int max_iter, int size_buf, int seed, double* m1, double* m2)
{
    int m = rep;
    double h = step;
    double m1_local = 0.0, m2_local = 0.0;
#pragma omp parallel reduction(+: m1_local, m2_local)
    {
        int rank = omp_get_thread_num();
        VSLStreamStatePtr s;
        vslNewStream(&s, VSL_BRNG_MCG31, seed+rank);
        double* w = malloc(size_buf * sizeof(double));
#pragma omp for schedule(static)
        for (int i = 0; i < m; i++)
        {
            double v = samp_single_em_2(x, y, h, type_bound, max_iter, size_buf, s, w);
            m1_local += v;
            m2_local += v*v;
        }
        free(w);
        vslDeleteStream(&s);
    }
    *m1 = m1_local / m;
    *m2 = m2_local / m;
    return ;
}

double samp_single_em_ml_1(double x, double y, double step, int num_step, int max_iter, int size_buf, VSLStreamStatePtr s, double* work)
{
    double h = step * num_step, h_fine = step, *w = work;
    int ctr_w = size_buf;
    double a = 0.0, a_fine = 0.0, f = x*x + y*y + 1.0, f_fine = x*x + y*y + 1.0;
    double x_fine = x, y_fine = y;
    int flag = 0;
    for (int i = 0; i < max_iter; i++)
    {
        double w_x_acc = 0.0, w_y_acc = 0.0;
        for (int j = 0; j < num_step; j++)
        {
            if (ctr_w >= size_buf)
            {
                vdRngGaussian(VSL_RNG_METHOD_GAUSSIAN_ICDF, s, size_buf, w, 0.0, 1.0);
                ctr_w = 0;
            }
            w_x_acc += w[ctr_w], w_y_acc += w[ctr_w+1];
            if (!(flag&1))
            {
                double
                    x_fine_new = x_fine + h_fine * x_fine + sqrt(h_fine) * w[ctr_w],
                    y_fine_new = y_fine + h_fine * y_fine + sqrt(h_fine) * w[ctr_w+1];
                double f_fine_new = x_fine_new*x_fine_new + y_fine_new*y_fine_new + 1.0;
                if (x_fine_new*x_fine_new + y_fine_new*y_fine_new > 1.0)
                    flag |= 1;
                else
                {
                    a_fine += h_fine * (f_fine + f_fine_new) / 2.0;
                    x_fine = x_fine_new, y_fine = y_fine_new;
                    f_fine = f_fine_new;
                }
            }
            ctr_w += 2;
        }
        if (!(flag&2))
        {
            double
                x_new = x + h * x + sqrt(h_fine) * w_x_acc,
                y_new = y + h * y + sqrt(h_fine) * w_y_acc;
            double f_new = x_new*x_new + y_new*y_new + 1.0;
            if (x_new*x_new + y_new*y_new > 1.0)
                flag |= 2;
            else
            {
                a += h * (f + f_new) / 2.0;
                x = x_new, y = y_new;
                f = f_new;
            }
        }
        if (flag == 3)
            break;
    }
    double delta_v = a - a_fine;
    return delta_v;
}

void driver_em_ml_1(double x, double y, double step, int num_step, int rep, int max_iter, int size_buf, int seed, double* m1, double* m2)
{
    int m = rep;
    double h = step;
    double m1_local = 0.0, m2_local = 0.0;
#pragma omp parallel reduction(+: m1_local, m2_local)
    {
        int rank = omp_get_thread_num();
        VSLStreamStatePtr s;
        vslNewStream(&s, VSL_BRNG_MCG31, seed+rank);
        double* w = malloc(size_buf * sizeof(double));
#pragma omp for schedule(static)
        for (int i = 0; i < m; i++)
        {
            double v = samp_single_em_ml_1(x, y, h, num_step, max_iter, size_buf, s, w);
            m1_local += v;
            m2_local += v*v;
        }
        free(w);
        vslDeleteStream(&s);
    }
    *m1 = m1_local / m;
    *m2 = m2_local / m;
    return ;
}
