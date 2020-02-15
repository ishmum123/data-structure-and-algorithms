from random import random
from time import time

from Utils import get_random_numbers, measure


class Node:

    def __init__(self, key, data=None) -> None:
        self.key = key
        self.data = data
        self.right = BinarySearchTree()
        self.left = BinarySearchTree()

    def __str__(self) -> str:
        return '(Key: ' + str(self.key) + '; Data: ' + str(self.data) + ')'


class AVLNode(Node):

    def __init__(self, key, data=None) -> None:
        super().__init__(key, data)
        self.right = AVLTree()
        self.left = AVLTree()


class BinarySearchTree:

    def __init__(self, node=None):
        self.node = node

    def insert(self, node):
        if not self.node or node.key == self.node.key:
            self.node = node
        elif node.key > self.node.key:
            self.node.right.insert(node)
        else:
            self.node.left.insert(node)

    def search(self, key):
        if not self.node or key == self.node.key:
            return self.node
        if key > self.node.key:
            return self.node.right.search(key)
        return self.node.left.search(key)


class DepthHoldingNode(Node):

    def __init__(self, key) -> None:
        super().__init__(key)
        self.depth_right = 0
        self.depth_left = 0


class AVLTree(BinarySearchTree):

    def __init__(self, node=None):
        super().__init__(node)
        self.calculate_depths()

    def calculate_depths(self):
        if self.node:
            self.depth_left = max(self.node.left.depth_left, self.node.left.depth_right) + 1
            self.depth_right = max(self.node.right.depth_left, self.node.right.depth_right) + 1
        else:
            self.depth_left = -1
            self.depth_right = -1

    def rotate_right(self):
        # Gather All values
        tree = self
        root = tree.node
        left_tree = root.left
        left_node = left_tree.node
        left_right_tree = left_node.right

        # Rotate
        tree.node = left_node
        left_node.right = left_tree
        left_tree.node = root
        root.left = left_right_tree

        # Recalculate depths
        left_tree.calculate_depths()
        self.calculate_depths()

    def rotate_left(self):
        # Gather All values
        tree = self
        root = tree.node
        right_tree = root.right
        right_node = right_tree.node
        right_left_tree = right_node.left

        # Rotate
        tree.node = right_node
        right_node.left = right_tree
        right_tree.node = root
        root.right = right_left_tree

        # Recalculate depths
        right_tree.calculate_depths()
        self.calculate_depths()

    def insert(self, node):
        super().insert(node)
        self.calculate_depths()
        if self.depth_left - 1 > self.depth_right:
            self.rotate_right()
        elif self.depth_right - 1 > self.depth_left:
            self.rotate_left()


def regular_bst(add, search):
    bst = BinarySearchTree()
    for n in add:
        bst.insert(Node(n))
    print(*dfs_inorder(bst))
    # return [bst.search(n) for n in search]


def avl_bst(add, search):
    bst = AVLTree()
    for n in add:
        bst.insert(AVLNode(n))
    print(*dfs_inorder(bst))
    # return [bst.search(n) for n in search]


def dfs_inorder(bst, arr=None):
    if arr is None:
        arr = []
    if not bst.node:
        return arr
    dfs_inorder(bst.node.left, arr)
    arr.append(bst.node.key)
    dfs_inorder(bst.node.right, arr)
    return arr


def dfs_preorder(bst, arr=None):
    if arr is None:
        arr = []
    if not bst.node:
        return arr
    arr.append(bst.node.key)
    dfs_preorder(bst.node.left, arr)
    dfs_preorder(bst.node.right, arr)
    return arr


def dfs_postorder(bst, arr=None):
    if arr is None:
        arr = []
    if not bst.node:
        return arr
    dfs_postorder(bst.node.left, arr)
    dfs_postorder(bst.node.right, arr)
    arr.append(bst.node.key)
    return arr


if __name__ == '__main__':
    # Binary Search Tree
    ul = 10 ** 4
    numbers_to_add = get_random_numbers(ul)
    numbers_to_search = get_random_numbers(ul)

    measure(lambda: regular_bst(numbers_to_add, numbers_to_search))
    measure(lambda: avl_bst(numbers_to_add, numbers_to_search))
