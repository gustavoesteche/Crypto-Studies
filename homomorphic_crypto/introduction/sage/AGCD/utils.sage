def sym_mod(a, n):
    a = ZZ(a) % n
    if 2*a > n:
        return a - n
    return a
def sym_mod_poly (poly , q):
    return Zx([ sym_mod(ZZ(ai), q) for ai in poly.list()])
def sym_mod_vec (vec , q):
    return [ sym_mod_poly (vi , q) for vi in vec]
