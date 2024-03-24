def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y
    
# it solves the bezout equation a * x + b * y = gcd

def inverse_pq(p:int, q:int):
    '''Find and returns the inverse of p mod q, and inverse of q mod p'''
    
    _, a, b = extended_gcd(p,q)
    return a,b

def fast_decryption(y: int,d:int, p:int, q:int, p_1:int, q_1:int) -> int:
    '''Using the Chinese Remainder Theorem and the Little Fermat theorem 
    its possible to come up with that small expression for fast decryption in RSA'''

    y_p, y_q = pow(y, d % (p-1),p), pow(y,d % (q-1), q)
    return (y_q * p_1 * p + y_p * q_1 * q) % (p*q)


p_1, q_1 = inverse_pq(11,13)
print(fast_decryption(15,103,11,13,p_1,q_1))

