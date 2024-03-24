#finding the public parameters for the diffie-helman kwy exchange

import sympy 
import random 
# use a algorithm to pick for a large prime of the order of 1024 bits

# brute force
def find_parameters(min_bits:int, max_bits:int):
    p = sympy.randprime(pow(2,min_bits), pow(2,max_bits)) # find a random prime within the range defined
    while(1):
        g = random.randrange(2,p)
        if sympy.is_primitive_root(g, p): # test if the random value g is a primitive root of the int-prime group p.
            return g,p
        
print(find_parameters(100,200))
