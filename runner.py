#!/usr/bin/env python3
import argparse
import subprocess
import sys
import tempfile
import shutil
import time
from pathlib import Path

def normalize(text):
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in text.split("\n")]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def detect_language(file_path):
    ext = file_path.suffix.lower()
    if ext == ".py":
        return "python"
    if ext == ".java":
        return "java"
    if ext in [".cpp", ".cc", ".cxx"]:
        return "cpp"
    return None

#edited run_command to return userDuration as well as timeout time
def run_command(cmd, cwd=None, stdin_data=None, timeout=10):
    start = time.time()
    try:
        result = subprocess.run(
            cmd,
            cwd=cwd,
            input=stdin_data,
            capture_output=True,
            timeout=timeout
        )
        duration = time.time() - start
        return result.returncode, result.stdout.decode(), result.stderr.decode(), duration
    except subprocess.TimeoutExpired:
        return 124, "", "TIMEOUT", timeout


def compile_cpp(file_path, build_dir):
    output_binary = build_dir / "prog"
    cmd = ["g++", "-O2", "-std=c++17", str(file_path), "-o", str(output_binary)]
    rc, out, err, _ = run_command(cmd)
    if rc != 0:
        return None, err
    return str(output_binary), None


def compile_java(file_path, build_dir):
    if file_path.name != "Main.java":
        return None, "Java file must be named Main.java"
    shutil.copy(file_path, build_dir / "Main.java")
    rc, out, err, _ = run_command(["javac", "Main.java"], cwd=build_dir)
    if rc != 0:
        return None, err
    return ["java", "-cp", str(build_dir), "Main"], None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--stdin", required=True)
    parser.add_argument("--expected", required=True)
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()

    submission = Path(args.file).resolve()
    input_file = Path(args.stdin).resolve()
    expected_file = Path(args.expected).resolve()

    if not submission.exists() or not input_file.exists() or not expected_file.exists():
        print("Missing required file.", file=sys.stderr)
        sys.exit(5)

    lang = detect_language(submission)
    if lang is None:
        print("Unsupported file type.", file=sys.stderr)
        sys.exit(5)

    stdin_data = input_file.read_bytes()
    expected_output = expected_file.read_text()

    with tempfile.TemporaryDirectory() as tmp:
        build_dir = Path(tmp)
        run_cwd = submission.parent

        if lang == "python":
            command = ["python3", str(submission)]

        elif lang == "cpp":
            binary, error = compile_cpp(submission, build_dir)
            if error:
                print(error, file=sys.stderr)
                sys.exit(2)
            command = [binary]

        elif lang == "java":
            command, error = compile_java(submission, build_dir)
            if error:
                print(error, file=sys.stderr)
                sys.exit(2)
            run_cwd = build_dir

        rc, stdout, stderr, duration = run_command(
            command,
            cwd=run_cwd,
            stdin_data=stdin_data,
            timeout=args.timeout
        )
        #changed here to include duration so I can use for scoreCalc

        if rc == 124:
            print("TIMEOUT", file=sys.stderr)
            sys.exit(4)

        if rc != 0:
            print("RUNTIME ERROR", file=sys.stderr)
            print(stderr, file=sys.stderr)
            sys.exit(3)


        if normalize(stdout) == normalize(expected_output):
            print(f"PASS")
            sys.exit(0)
        else:
            print("FAIL")
            print("=== expected ===")
            print(normalize(expected_output))
            print("=== actual ===")
            print(normalize(stdout))
            sys.exit(1)


if __name__ == "__main__":
    main()
