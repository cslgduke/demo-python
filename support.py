def print_func( par ):
    print ("Hello : ", par)
    return

def sum_func( *var_args_tuple ):
    sum = 0
    for var in var_args_tuple:
        sum += var
    return sum