class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def height(node):
    if node is None:
        return 0
    left_height = height(node.left)
    right_height = height(node.right)
    return max(left_height, right_height) + 1

def main():
    import sys
    input = sys.stdin.read().split()
    numbers = list(map(int, input))
    numbers = numbers[:-1]
    
    root = None
    for num in numbers:
        root = insert(root, num)
    
    print(height(root))

if __name__ == "__main__":
    main()