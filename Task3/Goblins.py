import sys
from collections import deque

def main():
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    
    front_deque = deque()
    back_deque = deque()
    
    output = []
    
    for _ in range(N):
        cmd = input[ptr]
        ptr += 1
        if cmd == '+':
            i = int(input[ptr])
            ptr += 1
            back_deque.append(i)
        elif cmd == '*':
            i = int(input[ptr])
            ptr += 1
            back_deque.appendleft(i)
        elif cmd == '-':
            if not front_deque:
                front_deque.append(back_deque.popleft())
            output.append(front_deque.popleft())
        
        # Балансировка деков
        if len(front_deque) < len(back_deque):
            front_deque.append(back_deque.popleft())
    
    print('\n'.join(map(str, output)))

if __name__ == "__main__":
    main()