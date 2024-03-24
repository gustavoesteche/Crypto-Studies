import sympy 
import random 

# Of course python is not a recommended language for any implementation
# of a cryptography algorithm, due to its slow execution, so its used for helping
# learning process.

def generate_key(end = 10e100, begin = 10e50) -> tuple[int]:
    ''' generating the keys using RSA algorithm, key_private = d
    key_public = (n,e)'''   

    def extended_gcd(a, b):
        ''' '''
        if b == 0:
            return a, 1, 0
        else:
            gcd, x, y = extended_gcd(b, a % b)
            return gcd, y, x - (a // b) * y
    
    def finding_e(phi_n):
        ''' '''
        while(1):
            e = random.randrange(1, (phi_n-1)//100)
            gcd,_,y = extended_gcd(phi_n, e)
            if gcd == 1 and y > 0: 
                return e, y
            
    p = sympy.randprime(begin, end)
    q = sympy.randprime(begin, end)
    
    n = p * q
    phi_n = n - p - q + 1
    
    e, d = finding_e(phi_n)

    return n,e,d

def encrypting(x:int, n:int, e:int):
    '''encrypting the integer x using RSA encrypting'''
    return pow(x,e,n)

def decrypting(y:int, d:int):
    '''dencrypting the integer y using RSA dencrypting'''
    return pow(y,d,n)

# testing the functionality of the code proposed for RSA

n,e,d = generate_key()
print(n, e,d)

x = 10
y = encrypting(x,n,e)

print(y)
print(decrypting(y,d))
