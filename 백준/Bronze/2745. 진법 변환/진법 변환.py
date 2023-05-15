A, B = input().split()
B = int(B)
result = 0

for i in range(len(A)):
    if A[i].isalpha():
        result += (ord(A[i])-55)*(B**(len(A)-i-1))
    else:
        result += int(A[i])*(B**(len(A)-i-1))

print(result)