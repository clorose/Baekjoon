#!/bin/bash

SOLVING_DIR="/app/solving"
cd "$SOLVING_DIR" || exit 1

if [ -z "$1" ]; then
    echo "사용법: ./run.sh [문제번호]"
    echo "예: ./run.sh 2460"
    exit 1
fi

PROBLEM="$1"
PROBLEM_DIR="${SOLVING_DIR}/${PROBLEM}"
PY_FILE="${PROBLEM_DIR}/main.py"
YAML_FILE="${PROBLEM_DIR}/input.yaml"

if [ ! -d "$PROBLEM_DIR" ]; then
    echo "오류: 디렉토리 '$PROBLEM_DIR' 가 존재하지 않습니다."
    exit 1
fi

if [ ! -f "$PY_FILE" ]; then
    echo "오류: main.py 파일이 '$PROBLEM_DIR'에 없습니다."
    exit 1
fi

if [ -f "$YAML_FILE" ]; then
    echo "✅ YAML 입력으로 '${PROBLEM}' 문제 실행"
    python test_runner.py "$PY_FILE" "$YAML_FILE"
else
    echo "⚠️  YAML 파일이 없습니다. '$PY_FILE' 단독 실행"
    python "$PY_FILE"
fi

echo "🔚 실행 완료: 문제 ${PROBLEM}"
