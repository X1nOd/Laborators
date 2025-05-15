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

def find_nodes_with_two_children(root, result):
    if root is None:
        return
    if root.left and root.right:
        result.append(root.value)
    find_nodes_with_two_children(root.left, result)
    find_nodes_with_two_children(root.right, result)

def main():
    import sys
    input = sys.stdin.read().split()
    numbers = list(map(int, input))
    numbers = numbers[:-1]
    
    root = None
    for num in numbers:
        root = insert(root, num)
    
    result = []
    find_nodes_with_two_children(root, result)
    result.sort()
    print('\n'.join(map(str, result)))

if __name__ == "__main__":
    main()