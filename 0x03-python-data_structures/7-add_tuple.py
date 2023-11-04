#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a_1 = tuple_a[1] if len(tuple_a) > 1 else 0
    b_0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b_1 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a_0 + b_0, a_1 + b_1)
