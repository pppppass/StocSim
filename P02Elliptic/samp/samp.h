#include <stdlib.h>
#include <math.h>
#include <mkl.h>
#include <Python.h>
#include <omp.h>

double solve_inter(double x0, double y0, double x1, double y1);

double samp_single_em_1(double x, double y, double step, int type_bound, int max_iter, int size_buf, VSLStreamStatePtr s, double* work);
double samp_single_em_2(double x, double y, double step, int type_bound, int max_iter, int size_buf, VSLStreamStatePtr s, double* work);

void driver_em_1(double x, double y, double step, int type_bound, int rep, int max_iter, int size_buf, int seed, double* m1, double* m2);
void driver_em_2(double x, double y, double step, int type_bound, int rep, int max_iter, int size_buf, int seed, double* m1, double* m2);

double samp_single_em_ml_1(double x, double y, double step, int num_step, int max_iter, int size_buf, VSLStreamStatePtr s, double* work);
void driver_em_ml_1(double x, double y, double step, int num_step, int rep, int max_iter, int size_buf, int seed, double* m1, double* m2);
