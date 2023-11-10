#include <Python.h>
#include <stdio.h>
#include <listobject.h>
#include <bytesobkect.h>

/**
 * print_python_list - printing list
 * @p: pointer to the list.
 */
void print_python_list(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("*] Python list info\n");
	printf("[*] Size of the Python List = %i\n", size);
	printf("[*] Allocated = %i\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		type = (list->ob_item[i])->ob_type->tp_name;
		printf("Element %i: %s\n", i, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - printing python bytes.
 * @p: pointer to the list.
 */
void print_python_bytes(PyObject *p)
{
	long int size;
	int i;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AaStringAndSize(p, &str, &size);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	if (size < 10)
		print("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");

	for (i = 0; i < size && i < 10; i++)
		printf(" %02hhx", str[i]);
	printf("\n");
}
