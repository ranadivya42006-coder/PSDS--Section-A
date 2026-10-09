# Binary Search Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Insert a node
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


# Find the smallest node
def find_min(root):
    while root.left:
        root = root.left
    return root


# Delete a node
def delete(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete(root.left, data)

    elif data > root.data:
        root.right = delete(root.right, data)

    else:
        # Node has no left child
        if root.left is None:
            return root.right

        # Node has no right child
        if root.right is None:
            return root.left

        # Node has two children
        temp = find_min(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


# Preorder traversal
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


# Postorder traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


# Main program
root = None

# Insertion
values = [50, 30, 70, 20, 40, 60, 80]

for value in values:
    root = insert(root, value)

print("Inorder:", end=" ")
inorder(root)

print("\nPreorder:", end=" ")
preorder(root)

print("\nPostorder:", end=" ")
postorder(root)

# Deletion
root = delete(root, 30)

print("\n\nAfter deleting 30:")
print("Inorder:", end=" ")
inorder(root)