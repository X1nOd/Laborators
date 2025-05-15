from collections import deque

def main():
    N = int(input())
    maze = [list(input().strip()) for _ in range(N)]
    row, col = map(int, input().split())
    row -= 1
    col -= 1

    if maze[row][col] != '.':
        print(0)
        return

    queue = deque()
    queue.append((row, col))
    maze[row][col] = '*'
    count = 1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and maze[nr][nc] == '.':
                maze[nr][nc] = '*'
                count += 1
                queue.append((nr, nc))

    print(count)

if __name__ == "__main__":
    main()