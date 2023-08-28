#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    temp_results = 0
    for i in range(0, list_length):
        try:
            temp_results = my_list_1[i] / my_list_2[i]
        except TypeError:
            temp_results = 0
            print("wrong type")
        except ZeroDivisionError:
            temp_results = 0
            print("division by 0")
        except IndexError:
            temp_results = 0
            print("out of range")
        finally:
            pass
        new_list.append(temp_results)
    return new_list
