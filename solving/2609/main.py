A, B = map(int, input().split())


def GCD(a, b):
    while b:
        a, b = b, a % b
    return a


GCD = GCD(A, B)
LCM = A * B // GCD

print(GCD)
print(LCM)
