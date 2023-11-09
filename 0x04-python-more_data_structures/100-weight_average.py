#!/usr/bin/python3
def weight_average(my_list=[]):

    w_values = list(map(lambda x: x[0] * x[1], my_list))
    total_weight = sum(map(lambda x: x[1], my_list))

    if total_weight == 0:
        return 0
    average = sum(w_values) / total_weight

    return average
