#include "samp.h"

static PyObject* wrapper_driver_samp_ising_single_2d(PyObject* self, PyObject* args)
{
    int n;
    double t, h;
    int iter, rep, size_buf, seed, thread;
    PyObject* sites_obj;

    if(!PyArg_ParseTuple(
        args, "iddiiiiiO!",
        &n, &t, &h, &iter, &rep, &size_buf, &seed, &thread,
        &PyArray_Type, &sites_obj
    ))
        return NULL;
    
    PyArrayObject* sites_arr = (PyArrayObject*)PyArray_FROM_OTF(sites_obj, NPY_INT, NPY_ARRAY_INOUT_ARRAY2);
    
    if (!sites_arr)
        return NULL;

    int* q = PyArray_DATA(sites_arr);

    omp_set_num_threads(thread);

    driver_samp_ising_single_2d(n, t, h, iter, rep, size_buf, seed, q);

    PyArray_ResolveWritebackIfCopy(sites_arr);
    Py_DECREF(sites_arr);

    return Py_BuildValue("");
}

static PyObject* wrapper_driver_samp_ising_2d(PyObject* self, PyObject* args)
{
    int n;
    double t, h;
    int iter, start, rep, size_buf, seed, thread;

    if(!PyArg_ParseTuple(
        args, "iddiiiiii",
        &n, &t, &h, &iter, &start, &rep, &size_buf, &seed, &thread
    ))
        return NULL;

    omp_set_num_threads(thread);

    double m1 = 0.0, m2 = 0.0, ma1 = 0.0, ma2 = 0.0, u1 = 0.0, u2 = 0.0, c1 = 0.0, c2 = 0.0;

    driver_samp_ising_2d(n, t, h, iter, start, rep, size_buf, seed, &m1, &m2, &ma1, &ma2, &u1, &u2, &c1, &c2);

    return Py_BuildValue("dddddddd", m1, m2, ma1, ma2, u1, u2, c1, c2);
}

static PyObject* wrapper_driver_samp_ising_kin_2d(PyObject* self, PyObject* args)
{
    int n;
    double t, h;
    int iter, start, rep, size_buf, seed, thread;

    if(!PyArg_ParseTuple(
        args, "iddiiiiii",
        &n, &t, &h, &iter, &start, &rep, &size_buf, &seed, &thread
    ))
        return NULL;

    omp_set_num_threads(thread);

    double m1 = 0.0, m2 = 0.0, ma1 = 0.0, ma2 = 0.0, u1 = 0.0, u2 = 0.0, c1 = 0.0, c2 = 0.0;

    driver_samp_ising_kin_2d(n, t, h, iter, start, rep, size_buf, seed, &m1, &m2, &ma1, &ma2, &u1, &u2, &c1, &c2);

    return Py_BuildValue("dddddddd", m1, m2, ma1, ma2, u1, u2, c1, c2);
}

static PyObject* wrapper_driver_samp_ising_kin_2d_corr(PyObject* self, PyObject* args)
{
    int n;
    double t, h;
    int iter, start, rep, size_buf, seed, thread;
    PyObject* g1_obj, * g2_obj, * ga1_obj, * ga2_obj;

    if(!PyArg_ParseTuple(
        args, "iddiiiiiiO!O!O!O!",
        &n, &t, &h, &iter, &start, &rep, &size_buf, &seed, &thread,
        &PyArray_Type, &g1_obj, &PyArray_Type, &g2_obj,
        &PyArray_Type, &ga1_obj, &PyArray_Type, &ga2_obj
    ))
        return NULL;
    
    PyArrayObject
        * g1_arr = (PyArrayObject*)PyArray_FROM_OTF(g1_obj, NPY_DOUBLE, NPY_ARRAY_INOUT_ARRAY2),
        * g2_arr = (PyArrayObject*)PyArray_FROM_OTF(g2_obj, NPY_DOUBLE, NPY_ARRAY_INOUT_ARRAY2),
        * ga1_arr = (PyArrayObject*)PyArray_FROM_OTF(ga1_obj, NPY_DOUBLE, NPY_ARRAY_INOUT_ARRAY2),
        * ga2_arr = (PyArrayObject*)PyArray_FROM_OTF(ga2_obj, NPY_DOUBLE, NPY_ARRAY_INOUT_ARRAY2);
    
    if (!g1_arr | !g2_arr | !ga1_arr | !ga2_arr)
        return NULL;

    double* g1 = PyArray_DATA(g1_arr), * g2 = PyArray_DATA(g2_arr), * ga1 = PyArray_DATA(ga1_arr), * ga2 = PyArray_DATA(ga2_arr);

    omp_set_num_threads(thread);

    driver_samp_ising_kin_2d_corr(n, t, h, iter, start, rep, size_buf, seed, g1, g2, ga1, ga2);

    PyArray_ResolveWritebackIfCopy(ga2_arr);
    Py_DECREF(ga2_arr);
    PyArray_ResolveWritebackIfCopy(ga1_arr);
    Py_DECREF(ga1_arr);
    PyArray_ResolveWritebackIfCopy(g2_arr);
    Py_DECREF(g2_arr);
    PyArray_ResolveWritebackIfCopy(g1_arr);
    Py_DECREF(g1_arr);

    return Py_BuildValue("");
}

static PyObject* wrapper_driver_samp_ising_kin_3d(PyObject* self, PyObject* args)
{
    int n;
    double t, h;
    int iter, start, rep, size_buf, seed, thread;

    if(!PyArg_ParseTuple(
        args, "iddiiiiii",
        &n, &t, &h, &iter, &start, &rep, &size_buf, &seed, &thread
    ))
        return NULL;

    omp_set_num_threads(thread);

    double m1 = 0.0, m2 = 0.0, ma1 = 0.0, ma2 = 0.0, u1 = 0.0, u2 = 0.0, c1 = 0.0, c2 = 0.0;

    driver_samp_ising_kin_3d(n, t, h, iter, start, rep, size_buf, seed, &m1, &m2, &ma1, &ma2, &u1, &u2, &c1, &c2);

    return Py_BuildValue("dddddddd", m1, m2, ma1, ma2, u1, u2, c1, c2);
}

static PyObject* wrapper_driver_samp_ising_kin_3d_corr(PyObject* self, PyObject* args)
{
    int n;
    double t, h;
    int iter, start, rep, size_buf, seed, thread;
    PyObject* g1_obj, * g2_obj, * ga1_obj, * ga2_obj;

    if(!PyArg_ParseTuple(
        args, "iddiiiiiiO!O!O!O!",
        &n, &t, &h, &iter, &start, &rep, &size_buf, &seed, &thread,
        &PyArray_Type, &g1_obj, &PyArray_Type, &g2_obj,
        &PyArray_Type, &ga1_obj, &PyArray_Type, &ga2_obj
    ))
        return NULL;
    
    PyArrayObject
        * g1_arr = (PyArrayObject*)PyArray_FROM_OTF(g1_obj, NPY_DOUBLE, NPY_ARRAY_INOUT_ARRAY2),
        * g2_arr = (PyArrayObject*)PyArray_FROM_OTF(g2_obj, NPY_DOUBLE, NPY_ARRAY_INOUT_ARRAY2),
        * ga1_arr = (PyArrayObject*)PyArray_FROM_OTF(ga1_obj, NPY_DOUBLE, NPY_ARRAY_INOUT_ARRAY2),
        * ga2_arr = (PyArrayObject*)PyArray_FROM_OTF(ga2_obj, NPY_DOUBLE, NPY_ARRAY_INOUT_ARRAY2);
    
    if (!g1_arr | !g2_arr | !ga1_arr | !ga2_arr)
        return NULL;

    double* g1 = PyArray_DATA(g1_arr), * g2 = PyArray_DATA(g2_arr), * ga1 = PyArray_DATA(ga1_arr), * ga2 = PyArray_DATA(ga2_arr);

    omp_set_num_threads(thread);

    driver_samp_ising_kin_3d_corr(n, t, h, iter, start, rep, size_buf, seed, g1, g2, ga1, ga2);

    PyArray_ResolveWritebackIfCopy(ga2_arr);
    Py_DECREF(ga2_arr);
    PyArray_ResolveWritebackIfCopy(ga1_arr);
    Py_DECREF(ga1_arr);
    PyArray_ResolveWritebackIfCopy(g2_arr);
    Py_DECREF(g2_arr);
    PyArray_ResolveWritebackIfCopy(g1_arr);
    Py_DECREF(g1_arr);

    return Py_BuildValue("");
}

static PyMethodDef methods[] = 
{
    {"wrapper_driver_samp_ising_2d", wrapper_driver_samp_ising_2d, METH_VARARGS, NULL},
    {"wrapper_driver_samp_ising_single_2d", wrapper_driver_samp_ising_single_2d, METH_VARARGS, NULL},
    {"wrapper_driver_samp_ising_kin_2d", wrapper_driver_samp_ising_kin_2d, METH_VARARGS, NULL},
    {"wrapper_driver_samp_ising_kin_2d_corr", wrapper_driver_samp_ising_kin_2d_corr, METH_VARARGS, NULL},
    {"wrapper_driver_samp_ising_kin_3d", wrapper_driver_samp_ising_kin_3d, METH_VARARGS, NULL},
    {"wrapper_driver_samp_ising_kin_3d_corr", wrapper_driver_samp_ising_kin_3d_corr, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef table = 
{
    PyModuleDef_HEAD_INIT,
    "samp", NULL, -1, methods
};

PyMODINIT_FUNC PyInit_samp(void)
{
    import_array();
    return PyModule_Create(&table);
}
