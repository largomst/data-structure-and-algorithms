from hashlib import new


class BinaryTree:
    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        if self.left == None:
            self.left = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left = self.left
            self.left = new_node

    def insert_right(self, value):
        if self.right == None:
            self.right = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right = self.right
            self.right = new_node

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_root_value(self, value):
        self.value = value

    def get_root_value(self):
        return self.value

    def preorder(self,):
        print(self.value)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()


def preorder(tree):
    if tree:
        print(tree.get_root_value())
        preorder(tree.get_left())
        preorder(tree.get_right())


def inorder(tree):
    if tree:
        inorder(tree.get_left())
        print(tree.get_root_value())
        inorder(tree.get_right())


def postorder(tree):
    if tree:
        postorder(tree.get_left())
        postorder(tree.get_right())
        print(tree.get_root_value())
