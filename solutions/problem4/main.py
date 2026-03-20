import sys

def solve():
    initial_message = sys.stdin.readline().strip()
    words_to_append = sys.stdin.readline().strip().split()

    message_words = initial_message.split()
    seen_words = set(message_words)
    
    for word in words_to_append:
        if word not in seen_words:
            message_words.append(word)
            seen_words.add(word)
    
    print(" ".join(message_words))

if __name__ == "__main__":
    solve()
