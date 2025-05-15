import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    adj = [[] for _ in range(n)]
    for i in range(n):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(n):
            if row[j] == 1:
                adj[i].append(j)

    visited = [False] * n
    parent = [-1] * n
    cycle = []

    def dfs(u):
        nonlocal cycle
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                parent[v] = u
                if dfs(v):
                    return True
            elif v != parent[u]:
                # Найден цикл
                cycle_start = v
                current = u
                cycle.append(cycle_start + 1)
                while current != cycle_start:
                    cycle.append(current + 1)
                    current = parent[current]
                return True
        return False

    for u in range(n):
        if not visited[u]:
            if dfs(u):
                print("YES")
                print(len(cycle))
                print(' '.join(map(str, cycle[::-1])))
                return

    print("NO")

if __name__ == "__main__":
    main()