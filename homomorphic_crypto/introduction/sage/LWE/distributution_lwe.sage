from sage.stats. distributions . discrete_gaussian_integer \
    import DiscreteGaussianDistributionIntegerSampler \
    as DiscreteGaussian

# imported the Discrete Gaussian to generate the noise of the dist

class LWE_distribution:
    def __init__(self, s, q, sigma = 2.3):
        self.n = len(s)  # s - secret key, q - ring of operations, sigma - dist medium
        self.s = s
        self.sigma = sigma
        self.D = DiscreteGaussian(sigma)
        self.Zq = ZZ.quotient(q)

    def random_noise(self):
        return vector([self.D() for _ in range(self.n)])

    def random_a(self):
        a = []
        for i in range(self.n):
            a.append([self.Zq.random_element() for _ in range(self.n)])
        return matrix(self.Zq, a)

    def sample(self):
        a = self.random_a()
        e = self.random_noise()
        b = self.s * a + e
        return a,b 
    
def sample_s(n, q):
    return vector([ZZ.random_element(0, q-1) for _ in range(n)])

LWE = LWE_distribution(sample_s(20, 10),10)
print(LWE.sample())

