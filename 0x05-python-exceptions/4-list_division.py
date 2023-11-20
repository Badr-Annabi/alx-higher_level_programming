#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        div = 0
        try:
            div = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
        except (ValueError, TypeError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            result.append(div)

    return result
