class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_and_get_depth(root, value):
    if root is None:
        return TreeNode(value), 1
    depth = 1
    current = root
    while True:
        if value < current.value:
            if current.left is None:
                current.left = TreeNode(value)
                return root, depth + 1
            else:
                current = current.left
                depth += 1
        elif value > current.value:
            if current.right is None:
                current.right = TreeNode(value)
                return root, depth + 1
            else:
                current = current.right
                depth += 1
        else:
            return root, None

def main():
    import sys
    input = sys.stdin.read().split()
    numbers = list(map(int, input))
    numbers = numbers[:-1]
    
    root = None
    depths = []
    for num in numbers:
        root, depth = insert_and_get_depth(root, num)
        if depth is not None:
            depths.append(depth)
    
    print('\n'.join(map(str, depths)))

if __name__ == "__main__":
    main()