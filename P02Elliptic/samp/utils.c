#include "samp.h"

double solve_inter(double x0, double y0, double x1, double y1)
{
    double
        a = (x1 - x0)*(x1 - x0) + (y1 - y0)*(y1 - y0),
        b = x0 * (x1 - x0) + y0 * (y1 - y0),
        c = x0*x0 + y0*y0 - 1.0;
    double t = (-b + sqrt(b*b - a * c)) / a;
    return t;
}
