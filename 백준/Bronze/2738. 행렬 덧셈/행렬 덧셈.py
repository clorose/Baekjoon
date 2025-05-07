N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]
    # *를 붙이면 언패킹하여 배열을 줄글로 출력한다.
    # " ".join(map(str,row)) 와 같음.
    print(*C[i])
