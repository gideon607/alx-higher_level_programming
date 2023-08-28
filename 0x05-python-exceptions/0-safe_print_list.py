#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    summing_total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            summing_total += 1
        except IndexError:
            break
    print()
    return(summing_total)
