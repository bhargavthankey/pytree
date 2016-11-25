from .node import Node


class BinarySearchTree:

    def _init_(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def insert_node(self, key, value=None):
        if value is None:
            value = key

        if self.root is None:
            self.root = Node(key, value)

        else:
            self._insert_node(key, value, self.root)

        self.size += 1

    def _insert_node(self, key, value, current_node):
        if current_node.key < key:
            if current_node.has_left_child():
                self._insert_node(key, value, current_node.left_child)
            else:
                current_node.left_child = Node(key, value, parent = current_node)
        else:
            if current_node.has_right_child():
                self._insert_node(key, value, current_node.right_child)

            else:
                current_node.left_child = Node(key, value, parent = current_node)

    def print_in_order(self, current_node):
        if current_node is not None:
            self.print_in_order(current_node.left_child)
            print('(' + str(current_node.key) + ' - ' +  str(current_node.value) + ')', end = ' ')
            self.print_in_order(current_node.right_child)

    def print_pre_order(self, current_node):
        if current_node is not None:
            print('(' + str(current_node.key) + ' - ' + str(current_node.value) + ')', end=' ')
            self.print_pre_order(current_node.left_child)
            self.print_pre_order(current_node.right_child)


    def print_post_order(self, current_node):
        if current_node is not None:
            self.print_pre_ordercurrent_node.left_child)
            self.print_post_order(current_node.right_child)
            print('(' + str(current_node.key) + ' - ' + str(current_node.value) + ')', end=' ')


