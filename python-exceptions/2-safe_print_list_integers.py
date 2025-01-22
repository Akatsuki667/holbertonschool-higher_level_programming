#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for idx in range(x):
        try:
            "{:d}".format(my_list[idx])
            count += 1
        except IndexError:
            break
        except (ValueError, TypeError):
            continue
        else:
            print("{:d}".format(my_list[idx]), end="")
    print()
    return count
