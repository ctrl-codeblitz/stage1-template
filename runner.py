#!/usr/bin/env python3
import argparse, subprocess, sys, tempfile, shutil, time, re
from pathlib import Path


def normalize(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and lines[-1] == "": lines.pop()
    return "\n".join(lines)


def detect_language(file_path):
    ext = file_path.suffix.lower()
    mapping = {".py": "python", ".java": "java", ".cpp": "cpp", ".cc": "cpp", ".cxx": "cpp"}
    return mapping.get(ext)


def extract_num(text):
    nums = re.findall(r'\d+', str(text))
    return nums[-1] if nums else "0"


def run_command(cmd, cwd=None, stdin_data=None, timeout=10):
    start = time.time()
    try:
        res = subprocess.run(cmd, cwd=cwd, input=stdin_data, capture_output=True, timeout=timeout)
        stdout = res.stdout.decode('utf-8', errors='replace')
        stderr = res.stderr.decode('utf-8', errors='replace')
        return res.returncode, stdout, stderr, time.time() - start
    except subprocess.TimeoutExpired:
        return 124, "", "TIMEOUT", timeout


def compile_cpp(file_path, build_dir):
    out_bin = build_dir / ("prog.exe" if sys.platform == "win32" else "prog")
    rc, _, err, _ = run_command(["g++", "-O2", "-std=c++17", str(file_path), "-o", str(out_bin)])
    return (str(out_bin), None) if rc == 0 else (None, err)


def compile_java(file_path, build_dir):
    if file_path.name != "starter.java": return None, "Java file must be named starter.java"
    shutil.copy(file_path, build_dir / "starter.java")
    rc, _, err, _ = run_command(["javac", "starter.java"], cwd=build_dir)
    return (["java", "-cp", str(build_dir), "starter"], None) if rc == 0 else (None, err)


def run_test_logic(sub, infile, expfile, timeout):
    if not sub or not sub.exists() or sub.stat().st_size == 0:
        return "MISSING", "", 0

    if not infile.exists() or not expfile.exists():
        return "SKIPPED", "Missing expected file", 0

    lang = detect_language(sub)
    with tempfile.TemporaryDirectory() as tmp:
        build_dir, run_cwd = Path(tmp), sub.parent

        if lang == "python":
            command = [sys.executable, str(sub)]
        elif lang == "cpp":
            command_str, err = compile_cpp(sub, build_dir)
            if err: return "COMPILE_ERROR", err, 0
            command = [command_str]
        elif lang == "java":
            command, err = compile_java(sub, build_dir)
            if err: return "COMPILE_ERROR", err, 0
            run_cwd = build_dir
        else:
            return "UNSUPPORTED", "", 0

        rc, stdout, stderr, dur = run_command(command, run_cwd, infile.read_bytes(), timeout)

        if rc == 124: return "TIMEOUT", "", dur
        if rc != 0: return "RUNTIME_ERROR", stderr, dur

        actual, expected = normalize(stdout), normalize(expfile.read_text())
        if actual == expected:
            return "PASS", "", dur
        else:
            return "FAIL", (expected, actual), dur


def print_result(infile_name, status, details, dur):
    if status == "PASS":
        print(f"  {infile_name}: PASS ({dur:.3f}s)")
    elif status == "FAIL":
        expected, actual = details
        print(f"  {infile_name}: FAIL")
        print(f"    expected: {expected}")
        print(f"    actual:   {actual}")
    elif status == "MISSING":
        print(f"  {infile_name}: MISSING SOLUTION")
    elif status == "TIMEOUT":
        print(f"  {infile_name}: TIMEOUT ({dur:.1f}s)")
    elif status in ["COMPILE_ERROR", "RUNTIME_ERROR"]:
        print(f"  {infile_name}: {status.replace('_', ' ')}")
    else:
        print(f"  {infile_name}: {status}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", help="Base directory to grade (e.g., stage1)")
    parser.add_argument("--timeout", type=int, default=10)
    parser.add_argument("--all", action="store_true", help="Run ALL test cases for every problem")
    args = parser.parse_args()

    if args.dir:
        stage_dirs = [Path(args.dir)]
    else:
        stage_dirs = sorted([p for p in Path(".").glob('stage*') if p.is_dir()], key=lambda p: int(extract_num(p.name)))

    if not stage_dirs:
        print("No stage directories found.")
        return

    total_passed, total_tests = 0, 0

    for stage_dir in stage_dirs:
        print(f"========== Grading {stage_dir.name} ==========")
        test_folders = sorted(list(stage_dir.glob('**/tests/**/problem*')), key=lambda p: int(extract_num(p.name)))

        if not test_folders:
            print(f"No problem folders found in {stage_dir}/tests/")
            continue

        stage_passed, stage_total = 0, 0

        for test_dir in test_folders:
            prob_num = extract_num(test_dir.name)
            print(f"[P{prob_num}]")

            if args.all:
                test_cases = sorted(list(test_dir.glob("input*.txt")))
            else:
                default_test = test_dir / "input1.txt"
                test_cases = [default_test] if default_test.exists() else []

            sol_pattern = f"**/solutions/**/solution{prob_num}/**/*"
            potential_sols = [f for f in stage_dir.glob(sol_pattern) if f.suffix in ['.py', '.cpp', '.java'] and f.is_file()]
            sub = potential_sols[0] if potential_sols else None

            for infile in test_cases:
                stage_total += 1
                expfile = test_dir / infile.name.replace("input", "expected")

                status, details, dur = run_test_logic(sub, infile, expfile, args.timeout)
                print_result(infile.name, status, details, dur)

                if status == "PASS":
                    stage_passed += 1
        
        total_passed += stage_passed
        total_tests += stage_total
        print(f"----- {stage_dir.name} Summary: {stage_passed}/{stage_total} passed -----")


    print(f"\n========== Overall Summary ==========")
    print(f"Passed {total_passed} / {total_tests} tests")
    print(f"===================================")
    sys.exit(0 if total_passed == total_tests else 1)


if __name__ == "__main__":
    main()
