# extended eucledian algorithm

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y
    
# it solves the bezout equation a * x + b * y = gcd
    
# interesting idea its solving the multiplication inverse of fields using
# extended gcd (EEA), its complexity goes to O(n) aprox