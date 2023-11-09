#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - printing list
 * @p: pointer to the list.
 */
void print_python_list(PyObject *p)
{
	int allocated, size, i;
	const char *type;

	if (strcmp(type, "bytes") == 0)
	{
		printf("[*] Python list info\n");
		printf("[ERROR] Invalid List Object\n");
		return;
	}

	PyVarObject *var = (PyVarObject *)p

	size = var->ob_size;
	allocated = (PyListObject *)p->allocated

	printf("*] Python list info\n");
	printf("[*] Size of the Python List = %ld", size);
	printf("[*] Allocated = %ld", allocated);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, type);
	}
}

/**
 * print_python_bytes - printing python bytes.
 * @p: pointer to the list.
 */
void print_python_bytes(PyObject *p)
{
	unsigned char i, size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("trying string: %s\n", butes->ob_sval);

	if (((PyVarObject *)p)->ob_size > 10)
		size = 10;
	else
		size = ((PyVarObject *)p)->ob_size + 1;
	printf("first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}

}
