#include <python.h>
#include <stdio.h>

/**
 * print_python_float - Function to give data of PyFloatObject
 * @p: The PyObject
 */
void print_python_list(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf(" [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
}
/**
 * print_python_bytes - The function will give data of the PyBytesObject
 * @p: The PyObject
 */
void print_python_bytes(PyObject *p)
{
	py_ssize_t size = 0, i = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf(" [ERROR] invalid Bytes object\n");
		return;
	}
	size = PyBytes_size(p);
	printf(" size: %zd\n", size);
	string = (assert(PyBytes_check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf(" trying string: %s\n", string);
	printf(" first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}
	printf("\n");
}

