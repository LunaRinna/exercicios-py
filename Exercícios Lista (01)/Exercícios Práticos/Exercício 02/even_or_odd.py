__author__ = "Luna Antunes"

def func_is_int(any_number):
    if isinstance(any_number, int) == False:
        return False
    else:
        return True, func_even_or_odd(any_number)

def func_even_or_odd(any_integer):
    if (any_integer % 2) == 0:
        return "Even"
    else:
        return "Odd"
