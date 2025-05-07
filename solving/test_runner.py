import sys
import subprocess
import yaml
import tempfile
import os

solution_path = sys.argv[1]
yaml_path = sys.argv[2]

# Load test cases from YAML
with open(yaml_path, "r", encoding="utf-8") as f:
    cases = yaml.safe_load(f)

# Tracking stats
pass_count = 0
fail_count = 0

# Run each test case
for idx, case in enumerate(cases, start=1):
    name = case.get("name", f"Case {idx}")
    input_data = case["input"]
    expected_output = case["expected"].strip().splitlines()

    # Write input to temp file
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
        tmp.write(input_data)
        tmp.flush()
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            ["python", solution_path],
            stdin=open(tmp_path),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=5,  # optional timeout
        )
    finally:
        os.unlink(tmp_path)  # clean up temp file

    actual_output = result.stdout.strip().splitlines()

    print(f"[{idx}] {name}")
    if actual_output == expected_output:
        print("✅ 통과\n")
        pass_count += 1
    else:
        print("❌ 실패")
        print("------ 예상 ------")
        print("\n".join(expected_output))
        print("------ 실제 ------")
        print("\n".join(actual_output))
        if result.stderr:
            print("------ stderr ------")
            print(result.stderr.strip())
        print()
        fail_count += 1

# Summary
print("🎯 테스트 요약")
print(f"  ✅ 통과: {pass_count}")
print(f"  ❌ 실패: {fail_count}")
print(f"  총합: {len(cases)}")
if fail_count == 0:
    print("🎉 모든 테스트를 통과했습니다!")
