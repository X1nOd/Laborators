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

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value)
        in_order_traversal(root.right)

def main():
    import sys
    input = sys.stdin.read().split()
    numbers = list(map(int, input))
    numbers = numbers[:-1]  # Убираем завершающий 0
    
    root = None
    for num in numbers:
        root = insert(root, num)
    
    in_order_traversal(root)

if __name__ == "__main__":
    main()