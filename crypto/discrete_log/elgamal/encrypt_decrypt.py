import sympy 
import random 

def find_parameters(min_bits:int, max_bits:int):
    p = sympy.randprime(pow(2,min_bits), pow(2,max_bits))
    while(1):
        g = random.randrange(2,p)
        if sympy.is_primitive_root(g, p):
            return g,p

def encrypting_elgamal(x:int, p:int, km:int) -> int: 
    return (x * km) % p

def decrypting_elgama(y:int, p:int, km_1:int) -> int:
    return (y * km_1) % p