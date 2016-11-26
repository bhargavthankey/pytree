from .node import Node


class BinarySearchTree:

    def __init__(self):
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
        if key < current_node.key:
            if current_node.has_left_child():
                self._insert_node(key, value, current_node.left_child)
            else:
                current_node.left_child = Node(key, value, parent = current_node)
        else:
            if current_node.has_right_child():
                self._insert_node(key, value, current_node.right_child)
            else:
                current_node.right_child = Node(key, value, parent = current_node)

    def __setitem__(self, key, value):
        self.insert_node(key, value)

    def print_in_order(self):
        self._in_order(self.root)

    def _in_order(self, current_node):
        if current_node is not None:
            self._in_order(current_node.left_child)
            print('(' + str(current_node.key) + ' - ' + str(current_node.value) + ')', end=' ')
            self._in_order(current_node.right_child)

    def print_pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, current_node):
        if current_node is not None:
            print('(' + str(current_node.key) + ' - ' + str(current_node.value) + ')', end=' ')
            self._pre_order(current_node.left_child)
            self._pre_order(current_node.right_child)

    def print_post_order(self):
        self._post_order(self.root)

    def _post_order(self, current_node):
        if current_node is not None:
            self._pre_order(current_node.left_child)
            self._post_order(current_node.right_child)
            print('(' + str(current_node.key) + ' - ' + str(current_node.value) + ')', end=' ')

    def search(self, key):
        if self.root:
            res = self._search(key, self.root)
            if res:
                return res.value
            else:
                return None
        else:
            return None

    def _search(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._search(key, current_node.left_child)
        else:
            return self._search(key, current_node.right_child)

    def __getitem__(self, key):
        return self.search(key)

    def __contains__(self, key):
        if self._search(key, self.root):
            return True
        else:
            return False

    def set_value(self, key, value):
        res = self.search(key)

        try:
            if res:
                return res.value
            else:
                raise KeyError('Key not found in the tree')

        except KeyError:
            print(KeyError)

    def delete_node(self, key):
        if self.size > 1:
            node_to_remove = self._search(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete_node(key)

    def remove(self, current_node):
        if current_node.is_leaf_node():  # leaf
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():  # interior
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.value = succ.value
        else:  # this node has one child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                current_node.left_child.value,
                                                current_node.left_child.left_child,
                                                current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                current_node.right_child.value,
                                                current_node.right_child.left_child,
                                                current_node.right_child.right_child)

    def splice_out(self):
        if self.is_leaf_node():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        current_node = self
        while current_node.has_left_child():
            current = current_node.left_child
        return current_node
