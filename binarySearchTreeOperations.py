import matplotlib.pyplot as plt


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self._insert_recursive(root.left, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, key)

        return root

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self._delete_recursive(root.left, key)
        elif key > root.key:
            root.right = self._delete_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            min_node = self._find_min(root.right)
            root.key = min_node.key
            root.right = self._delete_recursive(root.right, min_node.key)

        return root

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            return self._search_recursive(root.left, key)
        else:
            return self._search_recursive(root.right, key)

    def find_min(self):
        if self.root is None:
            return None
        return self._find_min(self.root)

    def _find_min(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root)

    def _find_max(self, root):
        current = root
        while current.right:
            current = current.right
        return current

    def visualize(self):
        if self.root is None:
            print("Tree is empty.")
            return

        fig, ax = plt.subplots()
        self._plot_tree(ax, self.root, 0, 0, 100)
        ax.set_aspect('equal')
        ax.axis('off')
        plt.show()

    def _plot_tree(self, ax, node, x, y, dx):
        if node:
            ax.plot([x], [y], 'o', color='black')  # Plot current node
            ax.text(x, y, str(node.key), verticalalignment='center', horizontalalignment='center',
                    fontsize=12)  # Label current node

            if node.left:
                ax.plot([x, x - dx], [y, y - 20], '-k')  # Plot left child edge
                self._plot_tree(ax, node.left, x - dx, y - 20, dx / 2)  # Recursively plot left subtree

            if node.right:
                ax.plot([x, x + dx], [y, y - 20], '-k')  # Plot right child edge
                self._plot_tree(ax, node.right, x + dx, y - 20, dx / 2)  # Recursively plot right subtree


# Example usage:
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(100)

print("Minimum:", bst.find_min().key)
print("Maximum:", bst.find_max().key)
print("Searching for 30:", bst.search(30).key if bst.search(30) else "Not found")
print("Searching for 100:", bst.search(100).key if bst.search(100) else "Not found")

bst.visualize()