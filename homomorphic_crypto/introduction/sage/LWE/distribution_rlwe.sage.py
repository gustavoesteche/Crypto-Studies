

# This file was *autogenerated* from the file distribution_rlwe.sage
from sage.all_cmdline import *   # import sage library

_sage_const_3p2 = RealNumber('3.2'); _sage_const_1 = Integer(1); _sage_const_24 = Integer(24); _sage_const_4 = Integer(4); _sage_const_2 = Integer(2); _sage_const_7 = Integer(7)
load("utils.sage")

from sage.stats. distributions . discrete_gaussian_integer     import DiscreteGaussianDistributionIntegerSampler     as DiscreteGaussian

Zx = ZZ['x']; (x,) = Zx._first_ngens(1)
class RLWE_distribution:
    def __init__(self, s, N, q, sigma=_sage_const_3p2 ):
        self.n = N 
        self.f = x**N + _sage_const_1  # assumindo que N é potencia de 2, polinômio ciclotônico
        self.s = s
        self.sigma = sigma 
        self.D = DiscreteGaussian(sigma)
        self.Zqx = ZZ.quotient(q)['x']
        self.Rq = self.Zqx.quotient(self.f)

    def random_noise(self):
        return  Zx([self.D() for _ in range(self.n)])

    def random_a(self):
        return self.Rq.random_element()

    def sample(self):
        s = self.s
        a = self.random_a () 
        e = self. random_noise ()
        b = (a*s + e) 
        return [a, b]

def inv_g_ZZ(a, B, q):
    a = sym_mod(ZZ(a), q)
    l = ceil(log(q, B))
    return vector(a.digits(base=B, padto=l))

print(inv_g_ZZ(-_sage_const_24 , _sage_const_4 , _sage_const_2 **_sage_const_7 ))
