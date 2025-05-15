n = int(input())
cars = list(map(int, input().split()))
stack = []
expected = 1
possible = True

for car in cars:
    while stack and stack[-1] == expected:
        expected += 1
        stack.pop()
    if car == expected:
        expected += 1
    else:
        stack.append(car)

while stack and stack[-1] == expected:
    expected += 1
    stack.pop()

print("YES" if expected == n + 1 else "NO")