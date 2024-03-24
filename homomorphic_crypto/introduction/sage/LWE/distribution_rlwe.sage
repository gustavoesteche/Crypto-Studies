load("utils.sage")

from sage.stats. distributions . discrete_gaussian_integer \
    import DiscreteGaussianDistributionIntegerSampler \
    as DiscreteGaussian

Zx.<x> = ZZ['x']
class RLWE_distribution:
    def __init__(self, s, N, q, sigma=3.2):
        self.n = N 
        self.f = x^N + 1 # assumindo que N é potencia de 2, polinômio ciclotônico
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

def inv_g_poly(a, B, q, n):
    l = ceil(log(q, B))
    result = vector(Zx, [0] * l)
    pow_x = 1
    for i in range(n):
        result += pow_x * inv_g_ZZ(a, B, q)
        pow_x *= x
    return result



