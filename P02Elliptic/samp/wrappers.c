#include "samp.h"

static PyObject* wrapper_driver_em_1(PyObject* self, PyObject* args)
{
    double x, y, step;
    int type_bound, rep, max_iter, size_buf, seed, thread;

    if(!PyArg_ParseTuple(
        args, "dddiiiiii",
        &x, &y, &step, &type_bound, &rep, &max_iter, &size_buf, &seed, &thread
    ))
        return NULL;

    omp_set_num_threads(thread);

    double m1, m2;

    driver_em_1(x, y, step, type_bound, rep, max_iter, size_buf, seed, &m1, &m2);

    return Py_BuildValue("dd", m1, m2);
}

static PyObject* wrapper_driver_em_2(PyObject* self, PyObject* args)
{
    double x, y, step;
    int type_bound, rep, max_iter, size_buf, seed, thread;

    if(!PyArg_ParseTuple(
        args, "dddiiiiii",
        &x, &y, &step, &type_bound, &rep, &max_iter, &size_buf, &seed, &thread
    ))
        return NULL;

    omp_set_num_threads(thread);

    double m1, m2;

    driver_em_2(x, y, step, type_bound, rep, max_iter, size_buf, seed, &m1, &m2);

    return Py_BuildValue("dd", m1, m2);
}

static PyObject* wrapper_driver_em_ml_1(PyObject* self, PyObject* args)
{
    double x, y, step;
    int num_step, rep, max_iter, size_buf, seed, thread;

    if(!PyArg_ParseTuple(
        args, "dddiiiiii",
        &x, &y, &step, &num_step, &rep, &max_iter, &size_buf, &seed, &thread
    ))
        return NULL;

    omp_set_num_threads(thread);

    double m1, m2;

    driver_em_ml_1(x, y, step, num_step, rep, max_iter, size_buf, seed, &m1, &m2);

    return Py_BuildValue("dd", m1, m2);
}

static PyMethodDef methods[] = 
{
    {"wrapper_driver_em_1", wrapper_driver_em_1, METH_VARARGS, NULL},
    {"wrapper_driver_em_2", wrapper_driver_em_2, METH_VARARGS, NULL},
    {"wrapper_driver_em_ml_1", wrapper_driver_em_ml_1, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef table = 
{
    PyModuleDef_HEAD_INIT,
    "samp", NULL, -1, methods
};

PyMODINIT_FUNC PyInit_samp(void)
{
    return PyModule_Create(&table);
}
