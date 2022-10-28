import random
from utils import *


class LWEPublicKey:
    def __init__(self, n, q, B):
        self.n = n
        self.q = q
        self.B = B

    def key_gen(self):
        A = sample_uniform_matrix(self.n, self.q)
        self.sk = sample_bounded_vector(self.n, self.B)
        As = matrix_vector_multiplication(A, self.sk, self.q)
        e = sample_bounded_vector(self.n, self.B)
        b = vector_vector_addition(As, e, self.q)
        self.pk = (A, b)

    def encrypt(self, m):
        (A, b) = self.pk
        r = sample_bounded_vector(self.n, self.B)
        e_prime = sample_bounded_vector(self.n, self.B)
        At = matrix_transpose(A)
        u = matrix_vector_multiplication(At, r, self.q)
        u = vector_vector_addition(u, e_prime, self.q)
        rAs = vector_vector_inner_product(r, b, self.q)
        e_prime_prime = sample_bounded_vector(1, self.B)[0]
        v = rAs + e_prime_prime % self.q
        v = (v + (self.q // 2) * m) % self.q
        return (u, v)

    def decrypt(self, ctx):
        (u, v) = ctx[0], ctx[1]
        s = self.sk
        rAs = vector_vector_inner_product(u, s, self.q)
        v = (v - rAs) % self.q
        return round(v / (self.q // 2)) % 2


if __name__ == "__main__":
    import time

    q = 3000
    n = 1000
    B = 5

    E = LWEPublicKey(n, q, B)

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
