# function for fast exponentiation multiply - square 
# square left shift
# multiply 1 at the rightmost position 


def fast_exponentiation1(base:int, exponent:int):
    ''' Fast eponentiation m-s using recursion'''
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_power = fast_exponentiation1(base, exponent // 2)
        return half_power * half_power
    else:
        half_power = fast_exponentiation1(base, (exponent - 1) // 2)
        return base * half_power * half_power


def fast_exponentiation(base:int, exponent:int):
    ''' Fast exponentiation m-s using left-right reading of bits'''
    exponent_ = bin(exponent)
    actual = 1
    for i in range(2,len(exponent_)):
        actual *= actual
        if exponent_[i] == '1':
            actual *= base
    
    return actual

