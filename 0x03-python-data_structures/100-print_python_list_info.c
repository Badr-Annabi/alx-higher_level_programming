#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic
 * info about Python lists.
 * @p: python object.
 * Return: nothing.
 */

void print_python_list_info(PyObject *p)
{
	int size, alloc, i;
	PyListObject *list = (PyListObject *)p;

	alloc = list->allocated;
	size = Py_SIZE(p);

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);

		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
