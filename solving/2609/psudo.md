# 최대공약수와 최소공배수

## 문제 번호
- [2609](https://www.acmicpc.net/problem/2609)


## 문제 해결 방법
- 두 수의 최대공약수(GCD)와 최소공배수(LCM)를 구하는 문제이다.
- 최대공약수는 유클리드 호제법을 사용하여 구할 수 있다.
- 최소공배수는 두 수의 곱을 최대공약수로 나누어 구할 수 있다.


## 의사코드
```md
변수 A, B = 입력받기

변수 GCD, LCM = 0

함수 GCD(A, B)
  만약 B == 0이면
    반환 A
  끝
  반환 GCD(B, A % B)
끝

GCD = GCD(A, B)
LCM = (A * B) / GCD
출력 GCD, LCM
```