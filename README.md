# 알고리즘 문제 풀이 저장소

이 저장소는 [BaekjoonHub](https://github.com/BaekjoonHub/BaekjoonHub)를 사용하여 자동으로 생성된 알고리즘 문제 풀이 모음입니다.

## 도커 환경 설정

동일한 개발 환경에서 알고리즘 문제를 풀기 위해 도커를 사용할 수 있습니다.

### 사용 방법

1. 도커 및 도커 컴포즈 설치 (https://docs.docker.com/get-docker/)
2. 터미널에서 다음 명령어 실행:

```bash
# 도커 이미지 빌드 및 컨테이너 실행 (별칭 사용 시)
dcub  # alias dcub="docker-compose up --build"
# 또는 전체 명령어
docker-compose up --build

# 컨테이너 접속 (별칭 사용 시)
dex baekjoon-boj-1  # 컨테이너 이름은 baekjoon-boj-1로 생성됨
# 또는 전체 명령어
docker exec -it baekjoon-boj-1 zsh
```

### 파일 구조

```
/
├── 백준/               # 백준 문제 풀이
├── 프로그래머스/        # 프로그래머스 문제 풀이
├── solving/           # 풀이 중인 문제 작업 공간
│   ├── solution.py    # 현재 작업 중인 문제 코드
│   └── input.txt      # 테스트 입력 데이터
├── zsh/                # ZSH 설정 파일
├── docker-compose.yml  # 도커 컴포즈 설정
├── Dockerfile          # 도커 이미지 설정
└── run.sh              # 문제 실행 스크립트
```

컨테이너 내부에서 모든 파일은 `/app` 디렉토리 아래에 마운트됩니다.

### 포함된 패키지
- Python 3.13 (Alpine 기반)
- ZSH 쉘 환경 (oh-my-zsh, powerlevel10k 테마)
- 개발 도구 (git, nano, curl, bash 등)
- Python 가상 환경 설정

### 백준 Python 환경 정보
- 언어 번호: 28
- 컴파일: `python3 -W ignore -c "import py_compile; py_compile.compile(r'Main.py')"`
- 실행: `python3 -W ignore Main.py`
- 버전: Python 3.13.1
- 시간 제한: ×3+2 초
- 메모리 제한: ×2+32 MB

## 문제 풀이 방법

### 실행 스크립트 사용하기

`/app/run.sh` 스크립트를 사용하여 Python 코드를 실행할 수 있습니다:

```bash
# solving 디렉토리 내에서 실행
./run.sh solution.py
```

스크립트는 자동으로 `input.txt` 파일이 있으면 입력으로 사용합니다.

### 수동으로 실행하기

```bash
# 컨테이너 내부에서
cd /app/solving
# Python 코드 실행
python my_solution.py < my_input.txt
```

## Python 코딩 팁

### 입력 받기

* 기본 입력:
```python
# 한 줄 입력받기
data = input()

# 공백을 기준으로 구분된 데이터를 입력 받을 때
data = list(map(int, input().split()))

# 공백을 기준으로 구분된 데이터가 많지 않다면 
a, b, c = map(int, input().split())
```

* 빠른 입력 (대용량 입력 처리 시):
```python
import sys

# 공백으로 구분된 숫자 입력 받기
N, M = map(int, sys.stdin.readline().split())

# 2차원 리스트 입력 받기
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 문자열 입력 받기 (개행문자 제거)
data = sys.stdin.readline().rstrip()
```

### 출력 팁

* f-string (Python 3.6 이상):
```python
answer = 5
print(f"정답은 {answer}입니다.")
```

* 리스트 출력시 대괄호 제거하기 (언패킹):
```python
result = [1, 2, 3]

# 기본 출력
print(result)  # [1, 2, 3]

# 언패킹으로 출력
print(*result)  # 1 2 3
```

### 자료구조 초기화

* N x M 크기의 이차원 리스트:
```python
# N x M 리스트 초기화 (방문 체크용)
n, m = 5, 5
visited = [[False] * m for _ in range(n)]

# 입력으로 2차원 배열 받기
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
```

### 파일로 입력 받기 (테스트용)

```python
import sys
sys.stdin = open("input.txt", "r")

# 이후 일반적인 입력 코드 사용
n, m = map(int, input().split())
```

또는 명령줄에서 입력 리다이렉션 사용:
```bash
python solution.py < input.txt
```

## 도커 환경에서 문제 풀기

1. 로컬 에디터에서 파일 작성 (예: `solving/solution.py`)
2. 컨테이너 접속:
   ```bash
   dex baekjoon-boj-1
   ```
3. 컨테이너 내부에서 코드 실행:
   ```bash
   cd /app/solving
   ./run.sh solution.py
   # 또는
   python solution.py < input.txt
   ```

ZSH 환경에서 여러 단축키와 자동완성 기능을 활용하여 더 효율적으로 문제를 풀 수 있습니다.