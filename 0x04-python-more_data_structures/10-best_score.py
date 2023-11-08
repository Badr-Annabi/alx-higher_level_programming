#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        sorted_dict = sorted(
                a_dictionary.items(), key=lambda item: item[1], reverse=True)
        return sorted_dict[0][0]
    else:
        return None
