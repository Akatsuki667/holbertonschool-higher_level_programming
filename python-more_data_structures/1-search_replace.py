#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for idx, item in enumerate(my_list):
        if item == search:
            my_list[idx] = replace
    return my_list
