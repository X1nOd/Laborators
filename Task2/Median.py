def find_median(A, B, L):
    merged = []
    i = j = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            merged.append(A[i])
            i += 1
        else:
            merged.append(B[j])
            j += 1
    merged.extend(A[i:])
    merged.extend(B[j:])
    return merged[L - 1]

N, L = map(int, input().split())
sequences = []
for _ in range(N):
    seq = list(map(int, input().split()))
    sequences.append(seq)

results = []
for i in range(N):
    for j in range(i + 1, N):
        A = sequences[i]
        B = sequences[j]
        median = find_median(A, B, L)
        results.append(str(median))

print('\n'.join(results))