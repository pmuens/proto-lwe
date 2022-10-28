import random


def sample_uniform_vector(n, q):
    return [random.randint(0, q - 1) for _ in range(n)]


def sample_bounded_vector(n, B):
    return [random.randint(-B, B) for _ in range(n)]


def sample_uniform_matrix(n, q):
    return [sample_uniform_vector(n, q) for _ in range(n)]


def sample_bounded_matrix(n, B):
    return [sample_bounded_vector(n, B) for _ in range(n)]


def matrix_vector_multiplication(m, v, q):
    n = len(m)
    return [sum(m[i][j] * v[j] for j in range(n)) % q for i in range(n)]


def vector_vector_addition(m, v, q):
    n = len(m)
    return [m[i] + v[i] % q for i in range(n)]


def vector_vector_inner_product(m, v, q):
    n = len(m)
    return sum(m[i] * v[i] for i in range(n)) % q


def matrix_matrix_multiplication(m, v, q):
    n = len(m)
    return [
        [sum(m[i][k] * v[k][j] for k in range(n)) % q for j in range(n)]
        for i in range(n)
    ]


def matrix_matrix_addition(m, v, q):
    n = len(m)
    return [[m[i][j] + v[i][j % q] for j in range(n)] for i in range(n)]


def matrix_transpose(m):
    n = len(m)
    return [[m[j][i] for j in range(n)] for i in range(n)]
