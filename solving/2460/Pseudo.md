# 지능형 기차 2

## 문제 링크
[백준 2460번 - 지능형 기차 2](https://www.acmicpc.net/problem/2460)

## 의사코드
```md
변수 현재인원 = 0
변수 최대인원 = 0

반복 10번
  내린 사람, 탄 사람 입력받기
  현재 인원 = 탄 사람 - 내린 사람
  현재 인원이 최대 인원보다 크면
    최대 인원 = 현재 인원

반복 끝
출력 최대 인원
```