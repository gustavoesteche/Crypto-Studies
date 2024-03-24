load("utils.sage")
load("distribution.sage")

class DGHV:
    def __init__(self, gamma, eta, rho, t=2, p=1):
        assert(gamma > eta)
        assert(eta > rho)
        if p == 1:
            p = random_prime(2^eta, lbound=2 ^ (eta-1))
        else:
            assert(eta - 1 <= p.nbits() <= eta)
        self.gamma = gamma 
        self.eta = eta
        self.rho = rho
        self.t = t
        self.p = p 
        self.x0 = p * sample_q(gamma, eta)
        self.Zp = ZZ.quotient(self.p)
        self.Zx0 = ZZ.quotient(self.x0)
        assert(self.x0 != 0)
    
    def enc(self, m):
        q = sample_q(self.gamma , self.eta)
        r = sample_r(self.rho)
        c = self.p*q + self.t * r + m
        c %= self.x0
        return c

    def dec(self, c): 
        return sym_mod(c, self.p) % self.t
    
    def not_gate(self, c):
        return (1-c) % self.x0

    def add(self, c1, c2):
        return (c1 + c2) % self.x0
    
    def mult(self, c1, c2):
        return (c1 *c2) % self.x0
        
def comparacao_homomorfica(dhgv:DGHV, n=3):
    m0 = ZZ.random_element(0, 2^n)
    m1 = ZZ.random_element(0, 2^n)
    print(m0 , m1)
    bits0 = m0.digits(base=2, padto = n)
    bits1 = m1.digits(base=2, padto = n)
    print(bits0, bits1)
    c0 = [dhgv.enc(bi) for bi in bits0]
    c1 = [dhgv.enc(bi) for bi in bits1]
    print(c0, c1)

    c, m = 1,1
    for i in range(n):
        cmp_i = dhgv.add(c0[i], c1[i])
        cmp_i = dhgv.not_gate(cmp_i)
        c = dhgv.mult(c, cmp_i)
        print("esse é o c: ", c)
    
    res = dhgv.dec(c)
    print(res)
    assert((m0 == m1) == res)

