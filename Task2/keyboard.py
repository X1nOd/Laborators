n = int(input())
c = list(map(int, input().split()))
k = int(input())
p = list(map(int, input().split()))

count = [0] * (n + 1)  # Индексация от 1 до n

for key in p:
    count[key] += 1

result = []
for i in range(1, n + 1):
    if count[i] > c[i - 1]:
        result.append("YES")
    else:
        result.append("NO")

print('\n'.join(result))