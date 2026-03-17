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


def get_problem_num(path):
    """Extracts digits from the parent folder name (e.g., solution14 -> 14)."""
    # Check the immediate folder name first
    folder_nums = re.findall(r'\d+', path.parent.name)
    if folder_nums:
        return folder_nums[0]
    # Fallback to searching the whole path
    path_nums = re.findall(r'\d+', str(path))
    return path_nums[0] if path_nums else "?"


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
    if file_path.name != "Main.java": return None, "Java file must be named Main.java"
    shutil.copy(file_path, build_dir / "Main.java")
    rc, _, err, _ = run_command(["javac", "Main.java"], cwd=build_dir)
    return (["java", "-cp", str(build_dir), "Main"], None) if rc == 0 else (None, err)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Solution file")
    parser.add_argument("--stdin", help="Input file")
    parser.add_argument("--expected", help="Expected file")
    parser.add_argument("--timeout", type=int, default=10)
    args = parser.parse_args()

    # 1. Detection
    sub_path = args.file
    if not sub_path:
        valid = [f for f in Path('.').glob('**/*') if f.suffix in ['.py', '.cpp', '.java']
                 and "solutions" in str(f).lower() and "problems" not in str(f).lower()]
        if not valid: return
        sub_path = valid[0]

    sub = Path(sub_path).resolve()
    prob_num = get_problem_num(sub)

    in_path = args.stdin or next(Path('.').glob('**/input1.txt'), None)
    exp_path = args.expected or next(Path('.').glob('**/expected1.txt'), None)

    if not all([sub, in_path, exp_path]): return
    infile, expfile = Path(in_path).resolve(), Path(exp_path).resolve()
    lang = detect_language(sub)

    # 2. Execution
    with tempfile.TemporaryDirectory() as tmp:
        build_dir = Path(tmp)
        run_cwd = sub.parent

        if lang == "python":
            command = [sys.executable, str(sub)]
        elif lang == "cpp":
            command_str, err = compile_cpp(sub, build_dir)
            if err: print(f"P{prob_num} COMPILE ERROR: {sub.name}\n{err}"); sys.exit(2)
            command = [command_str]
        elif lang == "java":
            command, err = compile_java(sub, build_dir)
            if err: print(f"P{prob_num} COMPILE ERROR: {sub.name}\n{err}"); sys.exit(2)
            run_cwd = build_dir

        rc, stdout, stderr, dur = run_command(command, run_cwd, infile.read_bytes(), args.timeout)

        # 3. Output with Problem Number
        prefix = f"[P{prob_num}] {infile.name}:"

        if rc == 124:
            print(f"{prefix} TIMEOUT ({args.timeout}s)")
            sys.exit(4)
        if rc != 0:
            print(f"{prefix} RUNTIME ERROR\n{stderr}")
            sys.exit(3)

        actual, expected = normalize(stdout), normalize(expfile.read_text())
        if actual == expected:
            print(f"{prefix} PASS ({dur:.3f}s)")
        else:
            print(f"{prefix} FAIL")
            print(f"  Exp: {expected}\n  Act: {actual}")
            sys.exit(1)


if __name__ == "__main__":
    main()
