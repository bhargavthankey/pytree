class Node:

    def __init__(self, key, value=None, left=None, right=None, parent=None):
        self.key = key
        if value is None:
            self.value = key
        else:
            self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_root_node(self):
        return self.parent

    def is_leaf_node(self):
        return not (self.right_child or self.left_child)

    def is_left_child(self):
        return self == self.parent.left_child

    def is_right_child(self):
        return self == self.parent.right_child

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def replace_node_data(self, key, value=None, left=None, right=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self

    def get_value(self, value):
        self.value = value

    def get_left_child(self, left):
        self.left_child = left
        self.left_child.parent = self

    def get_right_child(self, right):
        self.right_child = right
        self.right_child.parent = self

    def put_value(self):
        return self.value
