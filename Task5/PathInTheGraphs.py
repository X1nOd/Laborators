from collections import deque

def main():
    N = int(input())
    adj = [list(map(int, input().split())) for _ in range(N)]
    s, e = map(int, input().split())
    s -= 1
    e -= 1

    if s == e:
        print(0)
        return

    visited = [-1] * N
    parent = [-1] * N
    queue = deque([s])
    visited[s] = 0

    while queue:
        current = queue.popleft()
        for neighbor in range(N):
            if adj[current][neighbor] == 1 and visited[neighbor] == -1:
                visited[neighbor] = visited[current] + 1
                parent[neighbor] = current
                queue.append(neighbor)
                if neighbor == e:
                    break
        else:
            continue
        break

    if visited[e] == -1:
        print(-1)
    else:
        path = []
        current = e
        while current != -1:
            path.append(current + 1)
            current = parent[current]
        path.reverse()
        print(visited[e])
        print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()