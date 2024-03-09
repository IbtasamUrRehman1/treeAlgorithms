class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=', ')
        inorder_traversal(root.right)
def preorder_traversal(root):
    if root:
        print(root.val, end=', ')
        inorder_traversal(root.left)
        inorder_traversal(root.right)
def postorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        inorder_traversal(root.right)
        print(root.val, end=', ')
# Example Tree
#       1
#      / \
#     2   3
#   /  \ /  \
#  4   5 6  7

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


print("Inorder Traversal:", end=' ')
inorder_traversal(root)
print("\nPreorder Traversal:", end=' ')
preorder_traversal(root)
print("\nPostorder Traversal:", end=' ')
postorder_traversal(root)










