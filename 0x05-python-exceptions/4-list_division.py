#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_list = []
    for i in range(list_length):
        try:
            div_r = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('division by 0')
            div_r = 0
        except TypeError:
            print('wrong type')
            div_r = 0
        except IndexError:
            div_r = 0
            print('out of range')
        finally:
            div_list.append(div_r)
    return div_list
