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
    else:
        root.right = insert(root.right, value)
    return root

def find_second_largest(root):
    parent = None
    current = root
    
    while current.right:
        parent = current
        current = current.right
    
    if current.left:
        current = current.left
        while current.right:
            current = current.right
        return current.value
    else:
        return parent.value

def main():
    import sys
    input = sys.stdin.read().split()
    numbers = list(map(int, input))
    numbers = numbers[:-1]
    
    root = None
    for num in numbers:
        root = insert(root, num)
    
    print(find_second_largest(root))

if __name__ == "__main__":
    main()