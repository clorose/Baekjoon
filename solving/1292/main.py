A, B = map(int, input().split())

seq = []
i = 1

# extend는 리스트의 끝에 요소를 추가하는 메서드
# Append로 추가하면 배열로 추가되지만 extend는 요소를 추가한다.
while len(seq) < B:
    seq.extend([i] * i)
    i += 1

# seq = seq[A:B]
# A부터 B까지의 합을 구하기 위해 seq를 슬라이싱
print(sum(seq[A - 1 : B]))
