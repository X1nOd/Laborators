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

def find_leaves(root, leaves):
    if root is None:
        return
    if root.left is None and root.right is None:
        leaves.append(root.value)
    find_leaves(root.left, leaves)
    find_leaves(root.right, leaves)

def main():
    import sys
    input = sys.stdin.read().split()
    numbers = list(map(int, input))
    numbers = numbers[:-1]
    
    root = None
    for num in numbers:
        root = insert(root, num)
    
    leaves = []
    find_leaves(root, leaves)
    leaves.sort()
    print('\n'.join(map(str, leaves)))

if __name__ == "__main__":
    main()