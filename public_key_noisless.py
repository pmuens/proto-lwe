import random
from utils import *


class NoiselessPublicKey:
    def __init__(self, n, q):
        self.n = n
        self.q = q

    def key_gen(self):
        A = sample_uniform_matrix(self.n, self.q)
        self.sk = sample_uniform_vector(self.n, self.q)
        As = matrix_vector_multiplication(A, self.sk, self.q)
        self.pk = (A, As)

    def encrypt(self, m):
        (A, As) = self.pk
        r = sample_uniform_vector(self.n, self.q)
        At = matrix_transpose(A)
        u = matrix_vector_multiplication(At, r, self.q)
        rAs = vector_vector_inner_product(r, As, self.q)
        v = (rAs + m) % self.q
        return (u, v)

    def decrypt(self, ctx):
        (u, v) = ctx[0], ctx[1]
        s = self.sk
        rAs = vector_vector_inner_product(u, s, self.q)
        m = (v - rAs) % self.q
        return m


if __name__ == "__main__":
    import time

    q = 3000
    n = 1000

    E = NoiselessPublicKey(n, q)

    t = time.time()
    E.key_gen()
    t_keys = time.time()
    print(f"Generating keys took {t_keys-t} seconds...")

    m = random.randint(0, 1)
    print("Encrypting random message...")

    t = time.time()
    c = E.encrypt(m)
    t_enc = time.time()
    print(f"Encrypting took {t_enc-t} seconds...")

    t = time.time()
    m_prime = E.decrypt(c)
    t_dec = time.time()
    print(f"Decrypting took {t_dec-t} seconds...")

    assert m == m_prime

    print("Decrypting was successful!")
