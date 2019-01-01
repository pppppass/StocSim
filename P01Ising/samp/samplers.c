#include "samp.h"

void samp_ising_single_2d(int size, double temp, double bias, int iter, VSLStreamStatePtr s, int size_buf, int* work_int, double* work_dbl, int* site)
{
    int n = size;
    double t = temp, h = bias;

    int* q = site;
    int(* q_)[n] = q;
    int* w_int = work_int;
    double* w_dbl = work_dbl;
    int ctr_w = size_buf;
    viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, n*n, q, 0, 2);

    for (int i = 0; i < n*n; i++)
        q[i] = 2 * q[i] - 1;

    for (int i = 0; i < iter; i++)
    {
        if (ctr_w >= size_buf)
        {
            viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_int, 0, n*n);
            vdRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_dbl, 0.0, 1.0);
            ctr_w = 0;
        }
        int x = w_int[ctr_w] / n, y = w_int[ctr_w] % n;
        int 
            x_w = (x + n - 1) % n, x_e = (x + 1) % n,
            y_s = (y + n - 1) % n, y_n = (y + 1) % n;
        int d = -q_[x][y] * (q_[x_w][y] + q_[x_e][y] + q_[x][y_s] + q_[x][y_n]);
        double delta = -2.0 * d + 2.0 * q_[x][y] * h;
        if (w_dbl[ctr_w] < exp(-delta / t))
            q_[x][y] = -q_[x][y];
        ctr_w++;
    }

    return ;
}

void samp_ising_2d(int size, double temp, double bias, int iter, int start, VSLStreamStatePtr s, int size_buf, int* work_int, double* work_dbl, double* m, double* ma, double* u, double* c)
{
    int n = size;
    double t = temp, h = bias;

    int* q = work_int, * w_int = work_int + n*n;
    int(* q_)[n] = q;
    double* w_dbl = work_dbl;
    int ctr_w = size_buf;
    viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, n*n, q, 0, 2);

    int m_now = 0, h_now = 0;
    double m1 = 0.0, ma1 = 0.0, h1 = 0.0, h2 = 0.0;
    for (int i = 0; i < n*n; i++)
    {
        q[i] = 2 * q[i] - 1;
        m_now += q[i];
    }
    for (int x = 0; x < n; x++)
        for (int y = 0; y < n; y++)
        {
            int x_e = (x+1) % n, y_n = (y+1) % n;
            h_now -= q_[x][y] * (q_[x_e][y] + q_[x][y_n]);
        }

    for (int i = 0; i < iter; i++)
    {
        if (ctr_w >= size_buf)
        {
            viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_int, 0, n*n);
            vdRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_dbl, 0.0, 1.0);
            ctr_w = 0;
        }
        int x = w_int[ctr_w] / n, y = w_int[ctr_w] % n;
        int 
            x_w = (x + n - 1) % n, x_e = (x + 1) % n,
            y_s = (y + n - 1) % n, y_n = (y + 1) % n;
        int d = -q_[x][y] * (q_[x_w][y] + q_[x_e][y] + q_[x][y_s] + q_[x][y_n]);
        double delta = -2.0 * d + 2.0 * q_[x][y] * h;
        if (w_dbl[ctr_w] < exp(-delta / t))
        {
            m_now -= 2 * q_[x][y];
            h_now -= 2 * d;
            q_[x][y] = -q_[x][y];
        }
        if (i >= start)
            m1 += m_now, ma1 += fabs(m_now), h1 += h_now, h2 += h_now*h_now;
        ctr_w++;
    }

    m1 /= (iter - start), ma1 /= (iter - start), h1 /= (iter - start), h2 /= (iter - start);
    *m = m1 / (n*n), *ma = ma1 / (n*n), *u = h1 / (n*n), *c = (h2 - h1*h1) / (t*t) / (n*n);
    return ;
}

void samp_ising_kin_2d(int size, double temp, double bias, int iter, int start, VSLStreamStatePtr s, int size_buf, int* work_int, double* work_dbl, double* m, double* ma, double* u, double* c)
{
    int l = 65556;

    int n = size;
    double t = temp, h = bias;

    int* q = work_int, * q_c = work_int + n*n, * q_coor = work_int + 2*(n*n), * w_int = work_int + 13*(n*n);
    int(* c_stack)[n*n] = work_int + 3*(n*n);
    int(* q_)[n] = q, (* q_c_)[n] = q_c, (* q_coor_)[n] = q_coor;
    double* w_dbl = work_dbl;
    int ctr_w_int = size_buf, ctr_w_dbl = size_buf;
    viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, n*n, q, 0, 2);

    int ctr_c[10];
    for (int i = 0; i < 10; i++)
        ctr_c[i] = 0;
    double ds[10], ps[10], p_nows[10];
    for (int i = 0; i < 10; i++)
    {
        ds[i] = -(double)(2 * (i / 5) - 1) * (2 * (i % 5) - 4 + h);
        double delta = -2.0 * ds[i];
        ps[i] = fmin(exp(-delta / t), 1.0);
    }

    int m_now = 0, h_now = 0;
    double m1 = 0.0, ma1 = 0.0, h1 = 0.0, h2 = 0.0;
    double w_acc = 0.0;
    for (int i = 0; i < n*n; i++)
    {
        q[i] = 2 * q[i] - 1;
        m_now += q[i];
    }
    for (int x = 0; x < n; x++)
        for (int y = 0; y < n; y++)
        {
            int x_w = (x+n-1) % n, x_e = (x+1) % n, y_s = (y+n-1) % n, y_n = (y+1) % n;
            h_now -= q_[x][y] * (q_[x_e][y] + q_[x][y_n] + h);
            int c = (q_[x_w][y] + q_[x_e][y] + q_[x][y_s] + q_[x][y_n] + 5 * q_[x][y] + 9) / 2;
            q_c_[x][y] = c;
            q_coor_[x][y] = ctr_c[c];
            c_stack[c][ctr_c[c]++] = x*n + y;
        }

    for (int i = 0; i < iter; i++)
    {
        double p_sum = 0.0;
        for (int i = 0; i < 10; i++)
            p_sum += ps[i] * ctr_c[i];
        for (int i = 0; i < 10; i++)
            p_nows[i] = ps[i] * ctr_c[i] / p_sum;
        if (ctr_w_dbl >= size_buf)
        {
            vdRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_dbl, 0.0, 1.0);
            ctr_w_dbl = 0;
        }
        int c;
        double r = w_dbl[ctr_w_dbl++];
        for (c = 0; c < 9; c++)
            if (r < p_nows[c] || (r == p_nows[c] && p_nows[c] > 0.0))
                break;
            else
                r -= p_nows[c];
        int w_val, w_pos;
        while (1)
        {
            if (ctr_w_int >= size_buf)
            {
                viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_int, 0, l * n*n);
                ctr_w_int = 0;
            }
            w_pos = w_int[ctr_w_int++];
            if (w_pos >= l * n*n / ctr_c[c] * ctr_c[c])
                continue;
            else
            {
                w_pos = w_pos % ctr_c[c];
                break;
            }
        }
        w_val = c_stack[c][w_pos];
        int x = w_val / n, y = w_val % n;
        int q_now = q_[x][y];
        pop_and_push_2d(n, x, y, q_c, q_coor, ctr_c, c_stack, -5*q_now);
        int 
            x_w = (x + n - 1) % n, x_e = (x + 1) % n,
            y_s = (y + n - 1) % n, y_n = (y + 1) % n;
        pop_and_push_2d(n, x_w, y, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_2d(n, x_e, y, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_2d(n, x, y_s, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_2d(n, x, y_n, q_c, q_coor, ctr_c, c_stack, -q_now);

        m_now -= 2 * q_now;
        h_now -= 2 * ds[c];
        q_[x][y] = -q_[x][y];

        double w_now = 1.0 / ((double)(n*n) - p_sum);
        
        if (i >= start)
        {
            w_acc += w_now;
            m1 += m_now * w_now, ma1 += fabs(m_now) * w_now, h1 += h_now * w_now, h2 += h_now*h_now * w_now;
        }
    }

    m1 /= w_acc, ma1 /= w_acc, h1 /= w_acc, h2 /= w_acc;
    *m = m1 / (n*n), *ma = ma1 / (n*n), *u = h1 / (n*n), *c = (h2 - h1*h1) / (t*t) / (n*n);
    return ;
}

void samp_ising_kin_2d_corr(int size, double temp, double bias, int iter, int start, VSLStreamStatePtr s, int size_buf, int* work_int, double* work_dbl, double* g, double* a)
{
    int l = 65556;

    int n = size;
    double t = temp, h = bias;

    int* q = work_int, * q_c = work_int + n*n, * q_coor = work_int + 2*(n*n), * w_int = work_int + 13*(n*n);
    int(* c_stack)[n*n] = work_int + 3*(n*n);
    int(* q_)[n] = q, (* q_c_)[n] = q_c, (* q_coor_)[n] = q_coor;
    double* w_dbl = work_dbl;
    int ctr_w_int = size_buf, ctr_w_dbl = size_buf;
    viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, n*n, q, 0, 2);

    double g1[n];
    for (int i = 0; i < n; i++)
        g1[i] = 0.0;

    int ctr_c[10];
    for (int i = 0; i < 10; i++)
        ctr_c[i] = 0;
    double ds[10], ps[10], p_nows[10];
    for (int i = 0; i < 10; i++)
    {
        ds[i] = -(double)(2 * (i / 5) - 1) * (2 * (i % 5) - 4 + h);
        double delta = -2.0 * ds[i];
        ps[i] = fmin(exp(-delta / t), 1.0);
    }

    int m_now = 0;
    double m1 = 0.0, m2 = 0.0;
    double w_acc = 0.0;
    for (int i = 0; i < n*n; i++)
    {
        q[i] = 2 * q[i] - 1;
        m_now += q[i];
    }
    for (int x = 0; x < n; x++)
        for (int y = 0; y < n; y++)
        {
            int x_w = (x+n-1) % n, x_e = (x+1) % n, y_s = (y+n-1) % n, y_n = (y+1) % n;
            int c = (q_[x_w][y] + q_[x_e][y] + q_[x][y_s] + q_[x][y_n] + 5 * q_[x][y] + 9) / 2;
            q_c_[x][y] = c;
            q_coor_[x][y] = ctr_c[c];
            c_stack[c][ctr_c[c]++] = x*n + y;
        }

    for (int i = 0; i < iter; i++)
    {
        double p_sum = 0.0;
        for (int i = 0; i < 10; i++)
            p_sum += ps[i] * ctr_c[i];
        for (int i = 0; i < 10; i++)
            p_nows[i] = ps[i] * ctr_c[i] / p_sum;
        if (ctr_w_dbl >= size_buf)
        {
            vdRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_dbl, 0.0, 1.0);
            ctr_w_dbl = 0;
        }
        int c;
        double r = w_dbl[ctr_w_dbl++];
        for (c = 0; c < 9; c++)
            if (r < p_nows[c] || (r == p_nows[c] && p_nows[c] > 0.0))
                break;
            else
                r -= p_nows[c];
        int w_val, w_pos;
        while (1)
        {
            if (ctr_w_int >= size_buf)
            {
                viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_int, 0, l * n*n);
                ctr_w_int = 0;
            }
            w_pos = w_int[ctr_w_int++];
            if (w_pos >= l * n*n / ctr_c[c] * ctr_c[c])
                continue;
            else
            {
                w_pos = w_pos % ctr_c[c];
                break;
            }
        }
        w_val = c_stack[c][w_pos];
        int x = w_val / n, y = w_val % n;
        int q_now = q_[x][y];
        pop_and_push_2d(n, x, y, q_c, q_coor, ctr_c, c_stack, -5*q_now);
        int 
            x_w = (x + n - 1) % n, x_e = (x + 1) % n,
            y_s = (y + n - 1) % n, y_n = (y + 1) % n;
        pop_and_push_2d(n, x_w, y, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_2d(n, x_e, y, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_2d(n, x, y_s, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_2d(n, x, y_n, q_c, q_coor, ctr_c, c_stack, -q_now);

        m_now -= 2 * q_now;
        q_[x][y] = -q_[x][y];

        double w_now = 1.0 / ((double)(n*n) - p_sum);
        
        if (i >= start)
        {
            w_acc += w_now;
            m1 += m_now * w_now, m2 += m_now*m_now * w_now;
            int x = i % n, y = i / n % n;
            for (int j = 0; j < n; j++)
                g1[j] += w_now * q_[x][y] * q_[x][(y+j)%n];
        }
    }

    m1 /= w_acc, m2 /= w_acc;
    *a = m2 / (n*n) / (n*n);
    for (int i = 0; i < n; i++)
    {
        g1[i] /= w_acc;
        g[i] = g1[i];
    }
    return ;
}

void samp_ising_kin_3d(int size, double temp, double bias, int iter, int start, VSLStreamStatePtr s, int size_buf, int* work_int, double* work_dbl, double* m, double* ma, double* u, double* c)
{
    int l = 65556;

    int n = size;
    double t = temp, h = bias;

    int* q = work_int, * q_c = work_int + n*n*n, * q_coor = work_int + 2*(n*n*n), * w_int = work_int + 17*(n*n*n);
    int(* c_stack)[n*n*n] = work_int + 3*(n*n*n);
    int(* q_)[n][n] = q, (* q_c_)[n][n] = q_c, (* q_coor_)[n][n] = q_coor;
    double* w_dbl = work_dbl;
    int ctr_w_int = size_buf, ctr_w_dbl = size_buf;
    viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, n*n*n, q, 0, 2);

    int ctr_c[14];
    for (int i = 0; i < 14; i++)
        ctr_c[i] = 0;
    double ds[14], ps[14], p_nows[14];
    for (int i = 0; i < 14; i++)
    {
        ds[i] = -(double)(2 * (i / 7) - 1) * (2 * (i % 7) - 6 + h);
        double delta = -2.0 * ds[i];
        ps[i] = fmin(exp(-delta / t), 1.0);
    }

    int m_now = 0, h_now = 0;
    double m1 = 0.0, ma1 = 0.0, h1 = 0.0, h2 = 0.0;
    double w_acc = 0.0;
    for (int i = 0; i < n*n*n; i++)
    {
        q[i] = 2 * q[i] - 1;
        m_now += q[i];
    }
    for (int x = 0; x < n; x++)
        for (int y = 0; y < n; y++)
            for (int z = 0; z < n; z++)
            {
                int x_w = (x+n-1) % n, x_e = (x+1) % n, y_s = (y+n-1) % n, y_n = (y+1) % n, z_d = (z+n-1) % n, z_u = (z+1) % n;
                h_now -= q_[x][y][z] * (q_[x_e][y][z] + q_[x][y_n][z] + q_[x][y][z_u] + h);
                int c = (q_[x_w][y][z] + q_[x_e][y][z] + q_[x][y_s][z] + q_[x][y_n][z] + q_[x][y][z_d] + q_[x][y][z_u] + 7 * q_[x][y][z] + 13) / 2;
                q_c_[x][y][z] = c;
                q_coor_[x][y][z] = ctr_c[c];
                c_stack[c][ctr_c[c]++] = x*n*n + y*n + z;
            }

    for (int i = 0; i < iter; i++)
    {
        double p_sum = 0.0;
        for (int i = 0; i < 14; i++)
            p_sum += ps[i] * ctr_c[i];
        for (int i = 0; i < 14; i++)
            p_nows[i] = ps[i] * ctr_c[i] / p_sum;
        if (ctr_w_dbl >= size_buf)
        {
            vdRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_dbl, 0.0, 1.0);
            ctr_w_dbl = 0;
        }
        int c;
        double r = w_dbl[ctr_w_dbl++];
        for (c = 0; c < 13; c++)
            if (r < p_nows[c] || (r == p_nows[c] && p_nows[c] > 0.0))
                break;
            else
                r -= p_nows[c];
        int w_val, w_pos;
        while (1)
        {
            if (ctr_w_int >= size_buf)
            {
                viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_int, 0, l * n*n*n);
                ctr_w_int = 0;
            }
            w_pos = w_int[ctr_w_int++];
            if (w_pos >= l * n*n*n / ctr_c[c] * ctr_c[c])
                continue;
            else
            {
                w_pos = w_pos % ctr_c[c];
                break;
            }
        }
        w_val = c_stack[c][w_pos];
        int x = w_val / n / n, y = w_val / n % n, z = w_val % n;
        int q_now = q_[x][y][z];
        pop_and_push_3d(n, x, y, z, q_c, q_coor, ctr_c, c_stack, -7*q_now);
        int 
            x_w = (x+n-1) % n, x_e = (x+1) % n,
            y_s = (y+n-1) % n, y_n = (y+1) % n,
            z_d = (z+n-1) % n, z_u = (z+1) % n;
        pop_and_push_3d(n, x_w, y, z, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_3d(n, x_e, y, z, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_3d(n, x, y_s, z, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_3d(n, x, y_n, z, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_3d(n, x, y, z_d, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_3d(n, x, y, z_u, q_c, q_coor, ctr_c, c_stack, -q_now);

        m_now -= 2 * q_now;
        h_now -= 2 * ds[c];
        q_[x][y][z] = -q_[x][y][z];

        double w_now = 1.0 / ((double)(n*n*n) - p_sum);
        
        if (i >= start)
        {
            w_acc += w_now;
            m1 += m_now * w_now, ma1 += fabs(m_now) * w_now, h1 += h_now * w_now, h2 += h_now*h_now * w_now;
        }
    }

    m1 /= w_acc, ma1 /= w_acc, h1 /= w_acc, h2 /= w_acc;
    *m = m1 / (n*n*n), *ma = ma1 / (n*n*n), *u = h1 / (n*n*n), *c = (h2 - h1*h1) / (t*t) / (n*n*n);
    return ;
}

void samp_ising_kin_3d_corr(int size, double temp, double bias, int iter, int start, VSLStreamStatePtr s, int size_buf, int* work_int, double* work_dbl, double* g, double* a)
{
    int l = 65556;

    int n = size;
    double t = temp, h = bias;

    int* q = work_int, * q_c = work_int + n*n*n, * q_coor = work_int + 2*(n*n*n), * w_int = work_int + 17*(n*n*n);
    int(* c_stack)[n*n*n] = work_int + 3*(n*n*n);
    int(* q_)[n][n] = q, (* q_c_)[n][n] = q_c, (* q_coor_)[n][n] = q_coor;
    double* w_dbl = work_dbl;
    int ctr_w_int = size_buf, ctr_w_dbl = size_buf;
    viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, n*n*n, q, 0, 2);

    double g1[n];
    for (int i = 0; i < n; i++)
        g1[i] = 0.0;

    int ctr_c[14];
    for (int i = 0; i < 14; i++)
        ctr_c[i] = 0;
    double ds[14], ps[14], p_nows[14];
    for (int i = 0; i < 14; i++)
    {
        ds[i] = -(double)(2 * (i / 7) - 1) * (2 * (i % 7) - 6 + h);
        double delta = -2.0 * ds[i];
        ps[i] = fmin(exp(-delta / t), 1.0);
    }

    int m_now = 0;
    double m1 = 0.0, m2 = 0.0;
    double w_acc = 0.0;
    for (int i = 0; i < n*n*n; i++)
    {
        q[i] = 2 * q[i] - 1;
        m_now += q[i];
    }
    for (int x = 0; x < n; x++)
        for (int y = 0; y < n; y++)
            for (int z = 0; z < n; z++)
            {
                int x_w = (x+n-1) % n, x_e = (x+1) % n, y_s = (y+n-1) % n, y_n = (y+1) % n, z_d = (z+n-1) % n, z_u = (z+1) % n;
                int c = (q_[x_w][y][z] + q_[x_e][y][z] + q_[x][y_s][z] + q_[x][y_n][z] + q_[x][y][z_d] + q_[x][y][z_u] + 7 * q_[x][y][z] + 13) / 2;
                q_c_[x][y][z] = c;
                q_coor_[x][y][z] = ctr_c[c];
                c_stack[c][ctr_c[c]++] = x*n*n + y*n + z;
            }

    for (int i = 0; i < iter; i++)
    {
        double p_sum = 0.0;
        for (int i = 0; i < 14; i++)
            p_sum += ps[i] * ctr_c[i];
        for (int i = 0; i < 14; i++)
            p_nows[i] = ps[i] * ctr_c[i] / p_sum;
        if (ctr_w_dbl >= size_buf)
        {
            vdRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_dbl, 0.0, 1.0);
            ctr_w_dbl = 0;
        }
        int c;
        double r = w_dbl[ctr_w_dbl++];
        for (c = 0; c < 13; c++)
            if (r < p_nows[c] || (r == p_nows[c] && p_nows[c] > 0.0))
                break;
            else
                r -= p_nows[c];
        int w_val, w_pos;
        while (1)
        {
            if (ctr_w_int >= size_buf)
            {
                viRngUniform(VSL_RNG_METHOD_UNIFORM_STD, s, size_buf, w_int, 0, l * n*n*n);
                ctr_w_int = 0;
            }
            w_pos = w_int[ctr_w_int++];
            if (w_pos >= l * n*n*n / ctr_c[c] * ctr_c[c])
                continue;
            else
            {
                w_pos = w_pos % ctr_c[c];
                break;
            }
        }
        w_val = c_stack[c][w_pos];
        int x = w_val / n / n, y = w_val / n % n, z = w_val % n;
        int q_now = q_[x][y][z];
        pop_and_push_3d(n, x, y, z, q_c, q_coor, ctr_c, c_stack, -7*q_now);
        int 
            x_w = (x+n-1) % n, x_e = (x+1) % n,
            y_s = (y+n-1) % n, y_n = (y+1) % n,
            z_d = (z+n-1) % n, z_u = (z+1) % n;
        pop_and_push_3d(n, x_w, y, z, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_3d(n, x_e, y, z, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_3d(n, x, y_s, z, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_3d(n, x, y_n, z, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_3d(n, x, y, z_d, q_c, q_coor, ctr_c, c_stack, -q_now);
        pop_and_push_3d(n, x, y, z_u, q_c, q_coor, ctr_c, c_stack, -q_now);

        m_now -= 2 * q_now;
        q_[x][y][z] = -q_[x][y][z];

        // double w_now = 1.0 / ((double)(n*n*n) - p_sum);
        double w_now = 1.0;
        
        if (i >= start)
        {
            w_acc += w_now;
            m1 += m_now * w_now, m2 += m_now*m_now * w_now;
            int x = i % n, y = i / n % n, z = i / n / n % n;
            for (int j = 0; j < n; j++)
                g1[j] += w_now * q_[x][y][z] * q_[x][y][(z+j)%n];
        }
    }

    m1 /= w_acc, m2 /= w_acc;
    *a = m2 / (n*n*n) / (n*n*n);
    for (int i = 0; i < n; i++)
    {
        g1[i] /= w_acc;
        g[i] = g1[i];
    }
    return ;
}

void driver_samp_ising_single_2d(int size, double temp, double bias, int iter, int rep, int size_buf, int seed, int* sites)
{
    int n = size, m = rep;
    double t = temp, h = bias;
    int* q = sites;
#pragma omp parallel
    {
        int rank = omp_get_thread_num();
        VSLStreamStatePtr s;
        vslNewStream(&s, VSL_BRNG_MCG31, seed+rank);
        int* w_int = malloc(size_buf * sizeof(int));
        double* w_dbl = malloc(size_buf * sizeof(double));
#pragma omp for schedule(static)
        for (int i = 0; i < m; i++)
        {
            samp_ising_single_2d(n, t, h, iter, s, size_buf, w_int, w_dbl, q + i*(n*n));
        }
        free(w_int), free(w_dbl);
        vslDeleteStream(&s);
    }
    return ;
}

void driver_samp_ising_2d(int size, double temp, double bias, int iter, int start, int rep, int size_buf, int seed, double* m1, double* m2, double* ma1, double* ma2, double* u1, double* u2, double* c1, double* c2)
{
    int n = size, m = rep;
    double t = temp, h = bias;
#pragma omp parallel reduction(+: m1[:1], m2[:1], ma1[:1], ma2[:1], u1[:1], u2[:1], c1[:1], c2[:1])
    {
        int rank = omp_get_thread_num();
        VSLStreamStatePtr s;
        vslNewStream(&s, VSL_BRNG_MCG31, seed+rank);
        int* w_int = malloc((n*n + size_buf) * sizeof(int));
        double* w_dbl = malloc(size_buf * sizeof(double));
#pragma omp for schedule(static)
        for (int i = 0; i < m; i++)
        {
            double m, ma, u, c;
            samp_ising_2d(n, t, h, iter, start, s, size_buf, w_int, w_dbl, &m, &ma, &u, &c);
            m1[0] += m, m2[0] += m*m;
            ma1[0] += ma, ma2[0] += ma*ma;
            u1[0] += u, u2[0] += u*u;
            c1[0] += c, c2[0] += c*c;
        }
        free(w_int), free(w_dbl);
        vslDeleteStream(&s);
    }
    *m1 /= m, *m2 /= m;
    *ma1 /= m, *ma2 /= m;
    *u1 /= m, *u2 /= m;
    *c1 /= m, *c2 /= m;
    return ;
}

void driver_samp_ising_kin_2d(int size, double temp, double bias, int iter, int start, int rep, int size_buf, int seed, double* m1, double* m2, double* ma1, double* ma2, double* u1, double* u2, double* c1, double* c2)
{
    int n = size, m = rep;
    double t = temp, h = bias;
#pragma omp parallel reduction(+: m1[:1], m2[:1], ma1[:1], ma2[:1], u1[:1], u2[:1], c1[:1], c2[:1])
    {
        int rank = omp_get_thread_num();
        VSLStreamStatePtr s;
        vslNewStream(&s, VSL_BRNG_MCG31, seed+rank);
        int* w_int = malloc((13*(n*n) + size_buf) * sizeof(int));
        double* w_dbl = malloc(size_buf * sizeof(double));
#pragma omp for schedule(static)
        for (int i = 0; i < m; i++)
        {
            double m, ma, u, c;
            samp_ising_kin_2d(n, t, h, iter, start, s, size_buf, w_int, w_dbl, &m, &ma, &u, &c);
            m1[0] += m, m2[0] += m*m;
            ma1[0] += ma, ma2[0] += ma*ma;
            u1[0] += u, u2[0] += u*u;
            c1[0] += c, c2[0] += c*c;
        }
        free(w_int), free(w_dbl);
        vslDeleteStream(&s);
    }
    *m1 /= m, *m2 /= m;
    *ma1 /= m, *ma2 /= m;
    *u1 /= m, *u2 /= m;
    *c1 /= m, *c2 /= m;
    return ;
}

void driver_samp_ising_kin_2d_corr(int size, double temp, double bias, int iter, int start, int rep, int size_buf, int seed, double* g1, double* g2, double* ga1, double* ga2)
{
    int n = size, m = rep;
    double t = temp, h = bias;
#pragma omp parallel reduction(+: g1[:n], g2[:n])
    {
        int rank = omp_get_thread_num();
        VSLStreamStatePtr s;
        vslNewStream(&s, VSL_BRNG_MCG31, seed+rank);
        int* w_int = malloc((13*(n*n) + size_buf) * sizeof(int));
        double* w_dbl = malloc(size_buf * sizeof(double));
#pragma omp for schedule(static)
        for (int i = 0; i < m; i++)
        {
            double g[n], a;
            samp_ising_kin_2d_corr(n, t, h, iter, start, s, size_buf, w_int, w_dbl, g, &a);
            for (int j = 0; j < n; j++)
            {
                g1[j] += g[j], g2[j] += g[j]*g[j];
                ga1[j] += g[j] - a, ga2[j] += (g[j] - a)*(g[j] - a);

            }
        }
        free(w_int), free(w_dbl);
        vslDeleteStream(&s);
    }
    for (int i = 0; i < n; i++)
        g1[i] /= m, g2[i] /= m, ga1[i] /= m, ga2[i] /= m;
    return ;
}

void driver_samp_ising_kin_3d(int size, double temp, double bias, int iter, int start, int rep, int size_buf, int seed, double* m1, double* m2, double* ma1, double* ma2, double* u1, double* u2, double* c1, double* c2)
{
    int n = size, m = rep;
    double t = temp, h = bias;
#pragma omp parallel reduction(+: m1[:1], m2[:1], ma1[:1], ma2[:1], u1[:1], u2[:1], c1[:1], c2[:1])
    {
        int rank = omp_get_thread_num();
        VSLStreamStatePtr s;
        vslNewStream(&s, VSL_BRNG_MCG31, seed+rank);
        int* w_int = malloc((17*(n*n*n) + size_buf) * sizeof(int));
        double* w_dbl = malloc(size_buf * sizeof(double));
#pragma omp for schedule(static)
        for (int i = 0; i < m; i++)
        {
            double m, ma, u, c;
            samp_ising_kin_3d(n, t, h, iter, start, s, size_buf, w_int, w_dbl, &m, &ma, &u, &c);
            m1[0] += m, m2[0] += m*m;
            ma1[0] += ma, ma2[0] += ma*ma;
            u1[0] += u, u2[0] += u*u;
            c1[0] += c, c2[0] += c*c;
        }
        free(w_int), free(w_dbl);
        vslDeleteStream(&s);
    }
    *m1 /= m, *m2 /= m;
    *ma1 /= m, *ma2 /= m;
    *u1 /= m, *u2 /= m;
    *c1 /= m, *c2 /= m;
    return ;
}

void driver_samp_ising_kin_3d_corr(int size, double temp, double bias, int iter, int start, int rep, int size_buf, int seed, double* g1, double* g2, double* ga1, double* ga2)
{
    int n = size, m = rep;
    double t = temp, h = bias;
#pragma omp parallel reduction(+: g1[:n], g2[:n])
    {
        int rank = omp_get_thread_num();
        VSLStreamStatePtr s;
        vslNewStream(&s, VSL_BRNG_MCG31, seed+rank);
        int* w_int = malloc((17*(n*n*n) + size_buf) * sizeof(int));
        double* w_dbl = malloc(size_buf * sizeof(double));
#pragma omp for schedule(static)
        for (int i = 0; i < m; i++)
        {
            double g[n], a;
            samp_ising_kin_3d_corr(n, t, h, iter, start, s, size_buf, w_int, w_dbl, g, &a);
            for (int j = 0; j < n; j++)
            {
                g1[j] += g[j], g2[j] += g[j]*g[j];
                ga1[j] += g[j] - a, ga2[j] += (g[j] - a)*(g[j] - a);

            }
        }
        free(w_int), free(w_dbl);
        vslDeleteStream(&s);
    }
    for (int i = 0; i < n; i++)
        g1[i] /= m, g2[i] /= m, ga1[i] /= m, ga2[i] /= m;
    return ;
}
