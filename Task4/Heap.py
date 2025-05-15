def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N = int(input[ptr])
    ptr += 1
    heap = []
    output = []

    def sift_up(heap, idx):
        while idx > 0:
            parent = (idx - 1) // 2
            if heap[idx] > heap[parent]:
                heap[idx], heap[parent] = heap[parent], heap[idx]
                idx = parent
            else:
                break

    def sift_down(heap, idx):
        n = len(heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx
            if left < n and heap[left] > heap[largest]:
                largest = left
            if right < n and heap[right] > heap[largest]:
                largest = right
            if largest != idx:
                heap[idx], heap[largest] = heap[largest], heap[idx]
                idx = largest
            else:
                break

    for _ in range(N):
        cmd = input[ptr]
        ptr += 1
        if cmd == '0':
            k = int(input[ptr])
            ptr += 1
            heap.append(k)
            sift_up(heap, len(heap) - 1)
        elif cmd == '1':
            max_val = heap[0]
            heap[0] = heap[-1]
            heap.pop()
            if heap:
                sift_down(heap, 0)
            output.append(str(max_val))

    print('\n'.join(output))

if __name__ == "__main__":
    main()