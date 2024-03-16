import networkx as nx
import matplotlib.pyplot as plt


class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, root, key):
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if root is None:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.balance(root)

        if balance > 1 and self.balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance < -1 and self.balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete_key(self, key):
        self.root = self.delete(self.root, key)

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if root.key < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def search_key(self, key):
        return self.search(self.root, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.key, end=" ")
            self.inorder_traversal(root.right)

    def print_tree(self):
        self.inorder_traversal(self.root)

    def _build_graph(self, node, graph=None):
        if graph is None:
            graph = nx.DiGraph()

        if node:
            graph.add_node(node.key)
            if node.left:
                graph.add_edge(node.key, node.left.key)
                self._build_graph(node.left, graph)
            if node.right:
                graph.add_edge(node.key, node.right.key)
                self._build_graph(node.right, graph)

        return graph

    def visualize_tree(self):
        graph = self._build_graph(self.root)
        pos = nx.spring_layout(graph)
        nx.draw(graph, pos, with_labels=True, arrows=True)
        plt.show()


# Example usage:
avl_tree = AVLTree()
avl_tree.insert_key(10)
avl_tree.insert_key(20)
avl_tree.insert_key(30)
avl_tree.insert_key(40)
avl_tree.insert_key(50)
avl_tree.insert_key(25)

print("Original AVL Tree:")
avl_tree.visualize_tree()

avl_tree.delete_key(10)
print("AVL Tree after deleting 30:")
avl_tree.visualize_tree()

search_result = avl_tree.search_key(25)
if search_result:
    print("Key 25 found in the AVL Tree.")
else:
    print("Key 25 not found in the AVL Tree.")
