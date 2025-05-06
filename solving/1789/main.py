import math


def inverse_triangular(S):
    return int((math.sqrt(1 + 8 * S) - 1) / 2)


S = int(input())
print(inverse_triangular(S))
