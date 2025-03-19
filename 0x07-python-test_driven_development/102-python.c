#include <Python.h>
#include <stdio.h>

/**
 * print_python_string - Prints information about a Python string object.
 * @p: A pointer to the PyObject string.
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    wchar_t *value;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p))
        printf("  type: compact ascii\n");
    else
        printf("  type: compact unicode object\n");

    length = PyUnicode_GET_LENGTH(p);
    printf("  length: %ld\n", length);

    value = PyUnicode_AsWideCharString(p, &length);
    if (value == NULL)
    {
        printf("  [ERROR] Memory allocation failed\n");
        return;
    }

    printf("  value: %ls\n", value);
    PyMem_Free(value);
}
