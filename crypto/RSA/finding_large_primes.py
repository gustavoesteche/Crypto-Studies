# most part of algorithms that looks for large prime numbers 
# have a probabilistic nature 
import random

def fermats_test(p:int, s = 0):
    '''Fermats test takes advantage of the LFT, to check if the number is probably prime'''
    s = int(p * (0.2 + s))
    for i in range(s):
        if pow(random.randrange(2,p-2),p-1,p) != 1:
            return False # certainly false
    return True # probably true of course 

def miller_rabin_test(u: int, r: int, s: int = 100):
    ''' Miller rabin test takes advantage ok primes constructed like 2 ^ u * r + 1, because of 
    a theorem that says if r is odd, 2 properties must be satisfied for the number to be non-prime'''
    p = pow(2, u) * r + 1

    if r % 2 == 0:
        raise ValueError("r is an even number")

    for _ in range(s):
        a = random.randrange(2, p - 2)
        z = pow(a, r, p)
        if z != 1 and z != p - 1:
            for _ in range(u - 1):
                z = pow(z, 2, p)
                if z == 1:
                    return str(p) + " is composite" # certain 
            if z != p - 1:
                return str(p) + " is composite" # certain 
    return str(p) + " is likely prime" # probably true 

print(fermats_test(13,0))
print(miller_rabin_test(2,3))
