#Implement Binary tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursively(self.root, key)

    def _insert_recursively(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursively(current_node.left, key)
        else:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursively(current_node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_recursively(self.root, result)
        return result

    def _inorder_recursively(self, node, result):
        if node:
            self._inorder_recursively(node.left, result)
            result.append(node.key)
            self._inorder_recursively(node.right, result)

if __name__ == "__main__":
    binary_tree = BinaryTree()
    values = [5, 3, 8, 1, 4, 7, 9]

    for value in values:
        binary_tree.insert(value)

    print("Inorder Traversal:", binary_tree.inorder_traversal())

#Find height of a given tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def height_of_tree(root):
    if root is None:
        return -1

    left_subtree_height = height_of_tree(root.left)
    right_subtree_height = height_of_tree(root.right)

    return max(left_subtree_height, right_subtree_height) + 1

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Height of the binary tree:", height_of_tree(root))

#Perform Pre-order, Post-order, In-order traversal

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def pre_order_traversal(root):
    if root is not None:
        print(root.key, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.key, end=" ")
        in_order_traversal(root.right)

def post_order_traversal(root):
    if root is not None:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.key, end=" ")

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Pre-order Traversal:")
    pre_order_traversal(root)

    print("\nIn-order Traversal:")
    in_order_traversal(root)

    print("\nPost-order Traversal:")
    post_order_traversal(root)

# Function to print all the leaves in a given binary tree

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def print_leaves(root):
    if root is not None:
        if root.left is None and root.right is None:
            print(root.key, end=" ")
        print_leaves(root.left)
        print_leaves(root.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Leaves in the binary tree:")
    print_leaves(root)

#Implement BFS (Breath First Search) and DFS (Depth First Search)

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = [False] * len(self.graph)
        queue = [start]
        visited[start] = True

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

    def dfs(self, start):
        visited = [False] * len(self.graph)
        self._dfs_recursively(start, visited)

    def _dfs_recursively(self, node, visited):
        visited[node] = True
        print(node, end=" ")

        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self._dfs_recursively(neighbor, visited)

if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("BFS traversal starting from vertex 2:")
    g.bfs(2)

    print("\nDFS traversal starting from vertex 2:")
    g.dfs(2)

# Find sum of all left leaves in a given Binary Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def sum_of_left_leaves(root):
    def is_leaf(node):
        return node is not None and node.left is None and node.right is None

    if root is None:
        return 0

    left_sum = sum_of_left_leaves(root.left)
    right_sum = sum_of_left_leaves(root.right)

    if is_leaf(root.left):
        return root.left.key + left_sum + right_sum
    else:
        return left_sum + right_sum

if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)

    print("Sum of left leaves:", sum_of_left_leaves(root))

# Find sum of all nodes of the given perfect binary tree
def sum_of_perfect_binary_tree(height):
    total_nodes = 2**(height + 1) - 1
    return total_nodes

if __name__ == "__main__":
    height = 3
    total_sum = sum_of_perfect_binary_tree(height)
    print(f"Sum of all nodes in a perfect binary tree of height {height}: {total_sum}")

# Count subtress that sum up to a given value x in a binary tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def count_subtrees_with_sum(root, target_sum):
    def count_subtrees_recursively(node):
        nonlocal count

        if node is None:
            return 0

        left_sum = count_subtrees_recursively(node.left)
        right_sum = count_subtrees_recursively(node.right)
        current_sum = left_sum + right_sum + node.key

        if current_sum == target_sum:
            count += 1

        return current_sum

    count = 0
    count_subtrees_recursively(root)
    return count

if __name__ == "__main__":
    root = Node(10)
    root.left = Node(5)
    root.right = Node(-3)
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.right.right = Node(11)
    root.left.left.left = Node(3)
    root.left.left.right = Node(-2)
    root.left.right.right = Node(1)

    target_sum = 8
    result = count_subtrees_with_sum(root, target_sum)
    print(f"Number of subtrees with sum {target_sum}: {result}")

# Find maximum level sum in Binary Tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def max_level_sum(root):
    if root is None:
        return 0

    max_sum = root.key
    queue = [root]

    while queue:
        current_level_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)
            current_level_sum += node.key

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        max_sum = max(max_sum, current_level_sum)

    return max_sum

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(8)
    root.right.right.left = Node(6)
    root.right.right.right = Node(7)

    print("Maximum level sum:", max_level_sum(root))

# Print the nodes at odd levels of a tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def print_nodes_at_odd_levels(root):
    def print_odd_levels_recursively(node, level):
        if node is None:
            return

        if level % 2 != 0:
            print(node.key, end=" ")

        print_odd_levels_recursively(node.left, level + 1)
        print_odd_levels_recursively(node.right, level + 1)

    print_odd_levels_recursively(root, 1)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    print("Nodes at odd levels:")
    print_nodes_at_odd_levels(root)
