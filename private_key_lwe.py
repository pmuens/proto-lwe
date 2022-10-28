import random
from utils import *


class LWEPrivateKey:
    def __init__(self, n, q, B):
        self.n = n
        self.q = q
        self.B = B

    def key_gen(self):
        self.s = sample_uniform_vector(self.n, self.q)

    def encrypt(self, m):
        A = sample_uniform_matrix(self.n, self.q)
        e = sample_bounded_vector(self.n, self.B)
        b = matrix_vector_multiplication(A, self.s, self.q)
        b = vector_vector_addition(b, e, self.q)
        scaled_m = [(self.q // 2) * m[i] % self.q for i in range(self.n)]
        b = vector_vector_addition(b, scaled_m, self.q)
        return (A, b)

    def decrypt(self, ctx):
        (A, b) = ctx[0], ctx[1]
        As = matrix_vector_multiplication(A, self.s, self.q)

        for i in range(self.n):
            b[i] = (b[i] - As[i]) % self.q

        m = [0 for _ in range(self.n)]
        for i in range(self.n):
            m[i] = round(b[i] / (self.q // 2)) % 2

        return m


if __name__ == "__main__":
    import time

    q = 3000
    n = 1000
    B = 10

    E = LWEPrivateKey(n, q, B)

    t = time.time()
    E.key_gen()
    t_keys = time.time()
    print(f"Generating keys took {t_keys-t} seconds...")

    m = [random.randint(0, 1) for _ in range(n)]
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
