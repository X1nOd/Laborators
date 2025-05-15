import sys
from collections import defaultdict

def main():
    text = sys.stdin.read().split()
    word_counts = defaultdict(int)
    for word in text:
        word_counts[word] += 1
    
    max_count = max(word_counts.values())
    candidates = [word for word, count in word_counts.items() if count == max_count]
    candidates.sort()
    print(candidates[0])

if __name__ == "__main__":
    main()