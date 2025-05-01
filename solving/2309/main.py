from itertools import combinations

# 9명의 난쟁이 키 입력받기
heights = []
for _ in range(9):
    height = int(input())
    heights.append(height)

# 7명의 조합 중 합이 100인 경우 찾기
for comb in combinations(heights, 7):
    if sum(comb) == 100:
        # 오름차순 정렬
        result = sorted(comb)
        # 결과 출력
        for height in result:
            print(height)
        break  # 가능한 정답이 여러 가지인 경우 아무거나 출력하면 되므로 첫 번째 정답을 찾으면 종료