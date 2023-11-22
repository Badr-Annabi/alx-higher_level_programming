#!/usr/bin/python3
"""
Module Name: Singly linked list module

This module defines a node of a singly
linked list class.

Classes:
    Node: Defines a node of a singly linked list.
    SinglyLinkedList: Defines a SLL

Atrribute:
    None
Usage:
    Creating Nodes.
"""


class Node:
    """Represent a single Node for a SLL."""
    def __init__(self, data, next_node=None):

        """
        Initializes a new instance of Node class.

        Args:
            data (int): The data of the node.
            next_node: pointer to the next node

        Raises:
            TypeError: if the data is not integer,
            or next not is not an object
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
            Returning the node's data

            Return:
                the node's data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
            Sets the data

            Args:
                None

            Return:
                None
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
            Returning the next node

            Return:
                The next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
            Sets the next node

            Args:
                None

            Return:
                None
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a SLL (Singly Linked List)"""
    def __init__(self):
        """
        Initializes a new instance of singly linked list class.

        Args: None

        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts the new node and sorts the list.

        Args: value(the value of the new node)

        Return: None
        """
        new_node = Node(value)
        # if self.__head is None:
        #    new_node.next_node = None
        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """
        Defining our own print: prints all the list

        Args: None

        Return: All the nodes.
        """
        tmp = self.__head
        printed = ""
        while tmp is not None:
            printed += str(tmp.data) + "\n"
            tmp = tmp.next_node
        printed = printed.rstrip('\n')
        return printed
