
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height

def get_balance(node):
    if not node:
       return 0
    return height(node.left) - height(node.right)

def update_height(node):
    if node:
       node.height = 1 + max(height(node.left), height(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def insert(node, key):
    if not node:
       return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)
    else:
        return node

    update_height(node)
    balance = get_balance(node)

    if balance > 1:
        if key < node.left.key:
            return rotate_right(node)
        else:
            node.left = rotate_left(node.left)
            return rotate_right(node)
    if balance < -1:
        if key > node.right.key:
            return rotate_left(node)
        else:
            node.right = rotate_right(node.right)
            return rotate_left(node)
    return node

def min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete_node(root, key):
    if not root:
        return root
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = min_value_node(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    update_height(root)
    balance = get_balance(root)

    if balance > 1:
        if get_balance(root.left) >= 0:
            return rotate_right(root)
        else:
            root.left = rotate_left(root.left)
            return rotate_right(root)
    if balance < -1:
        if get_balance(root.right) <= 0:
            return rotate_left(root)
        else:
            root.right = rotate_right(root.right)
            return rotate_left(root)
    return root

def inorder_traversal(node):
    if not node:
        return []
    return inorder_traversal(node.left) + [node.key] + inorder_traversal(node.right)

def process_file(filename):
    root = None
    with open(filename, 'r') as file:
        lines = file.readlines()
        if len(lines) < 2:
            print("File should contain at least two lines.")
            return None

        insert_values = [int(x.strip()) for x in lines[0].split(',')]
        for value in insert_values:
            root = insert(root, value)

        print("After insertion:", inorder_traversal(root))

        delete_values = [int(x.strip()) for x in lines[1].split(',')]
        for value in delete_values:
            root = delete_node(root, value)

        print("After deletion:", inorder_traversal(root))

    return root

def write_avl_to_file(root, filename):
    with open(filename, 'w') as file:
        inorder_to_file(root, file)

def inorder_to_file(root, file, is_first=[True]):
    if root:
        inorder_to_file(root.left, file, is_first)
        if not is_first[0]:
            file.write(",")
        else:
            is_first[0] = False
        file.write(str(root.key))
        inorder_to_file(root.right, file, is_first)

input_filename = "C:\ADS&AA LAB\input.txt"
output_filename = "C:\ADS&AA LAB\output.txt"

root = process_file(input_filename)
if root:
    write_avl_to_file(root, output_filename)
    print(f"Final AVL tree has been written to '{output_filename}'")