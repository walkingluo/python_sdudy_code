# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class Tree:

    def __init__(self, node=None):
        self.root = node

    def print_tree(self, root):
        
        if root.left:
            self.print_tree(root.left)
        print(root.data)
        if root.right:
            self.print_tree(root.right)


if __name__ == '__main__':

    tree = Tree(TreeNode(10))
    tree.print_tree(tree.root)