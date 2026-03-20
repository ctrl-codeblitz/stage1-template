import sys

def solve():
    text = sys.stdin.readline().strip()
    vowels = "aeiouAEIOU"
    consonant_count = 0
    for char in text:
        if 'a' <= char.lower() <= 'z' and char not in vowels:
            consonant_count += 1
    print(consonant_count)

if __name__ == "__main__":
    solve()
