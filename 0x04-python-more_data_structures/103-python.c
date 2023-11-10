#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - print some basic info about
 * Python bytes object.
 *
 * @p: python object.
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int idx;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (idx = 0; idx <= size && idx < 10; idx++)
		printf(" %02hhx", str[idx]);
	printf("\n");

}

/**
 * print_python_list - print some basic info about
 * Python lists.
 *
 * @p: python object.
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int idx;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", list->allocated);
	for (idx = 0; idx < size; idx++)
	{
		type = (list->ob_item[idx])->ob_type->tp_name;
		printf("Element %i: %s\n", idx, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[idx]);
	}
}
