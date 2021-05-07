#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    score = 0
    name = ""
    new_list = list(a_dictionary)
    for k in new_list:
        if score < a_dictionary[k]:
            score = a_dictionary[k]
            name = k
    return name
