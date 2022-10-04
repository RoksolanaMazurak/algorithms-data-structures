class Node:
    def __init__(self, data=None):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = 1

    def __repr__(self):
        return str(self.data)


class AVLTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        if self.root is None:
            return ' '

        content = ' '
        cur_nodes = [self.root]
        cur_height = self.root.height
        sep = ' ' * (2 ** (cur_height - 1))

        while True:

            if len(cur_nodes) == 0:
                break

            cur_row = ''
            next_row = ''
            next_nodes = []

            if all(node is None for node in cur_nodes):
                break

            for node in cur_nodes:

                if node is None:
                    cur_row += '' + sep
                    next_row += '' + sep
                    next_nodes.extend([None, None])
                    continue

                if node.data is not None:
                    cur_row += '%s ' % (str(node.data))
                else:
                    cur_row += ''

                if node.left_child is not None:
                    next_nodes.append(node.left_child)
                    next_row += '/ '
                else:
                    next_row += '' + sep
                    next_nodes.append(None)

                if node.right_child is not None:
                    next_nodes.append(node.right_child)
                    next_row += '\\' + sep
                else:
                    next_row += ' ' + sep
                    next_nodes.append(None)

            content += (cur_height * '' + cur_row + '\n' + cur_height * '' + next_row + '\n')
            cur_nodes = next_nodes

        return content

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left_child is None:
                current_node.left_child = Node(data)
                current_node.left_child.parent = current_node  # set parent
            else:
                self._insert(data, current_node.left_child)
        elif data > current_node.data:
            if current_node.right_child is None:
                current_node.right_child = Node(data)
                current_node.right_child.parent = current_node  # set parent
            else:
                self._insert(data, current_node.right_child)
        else:
            print("Data is already exist!")

    def delete_data(self, data):
        return self.delete_node(self.find(data))

    def delete_node(self, node):

        if node is None or self.find(node.data) is None:
            print("No node to be deleted!")
            return None

        def num_children(node):
            children = 0
            if node.left_child is not None:
                children += 1
            if node.right_child is not None:
                children += 1
            return children

        node_parent = node.parent

        node_children = num_children(node)

        if node_children == 0:

            if node_parent is not None:
                if node_parent.left_child == node:
                    node_parent.left_child = None
                else:
                    node_parent.right_child = None
            else:
                self.root = None

        if node_children == 1:

            if node.left_child is not None:
                child = node.left_child
            else:
                child = node.right_child

            if node_parent is not None:
                if node_parent.left_child == node:
                    node_parent.left_child = child
                else:
                    node_parent.right_child = child
            else:
                self.root = child

            child.parent = node_parent

        def min_value_node(n):
            current = n
            while current.left_child is not None:
                current = current.left_child
            return current

        if node_children == 2:

            successor = min_value_node(node.right_child)

            node.data = successor.data

            self.delete_node(successor)
            return

        if node_parent is not None:
            node_parent.height = 1 + max(self.get_height(node_parent.left_child),
                                         self.get_height(node_parent.right_child))

            self._check_deletion(node_parent)

    def _check_deletion(self, current_node):
        if current_node is None:
            return

        left_height = self.get_height(current_node.left_child)
        right_height = self.get_height(current_node.right_child)

        if abs(left_height - right_height) > 1:
            y = self.more_height_child(current_node)
            x = self.more_height_child(y)
            self._balance_node(current_node, y, x)

        self._check_deletion(current_node.parent)

    def _balance_node(self, grandparent, parent, node):
        if parent == grandparent.left_child and node == parent.left_child:
            self._right_rotate(grandparent)

        elif parent == grandparent.right_child and node == parent.right_child:
            self._left_rotate(grandparent)

        elif parent == grandparent.left_child and node == parent.right_child:
            self._left_rotate(parent)
            self._right_rotate(grandparent)

        elif parent == grandparent.right_child and node == parent.left_child:
            self._right_rotate(parent)
            self._left_rotate(grandparent)
        else:
            raise Exception('No nodes to balance!')

    def _right_rotate(self, node):
        parent = node.parent
        child = node.left_child
        grandchild = child.right_child

        child.right_child = node
        node.parent = child
        node.left_child = grandchild

        if grandchild is not None:
            grandchild.parent = node
        child.parent = parent

        if child.parent is None:
            self.root = child
        else:
            if child.parent.left_child == node:
                child.parent.left_child = child
            else:
                child.parent.right_child = child
        node.height = 1 + max(self.get_height(node.left_child),
                              self.get_height(node.right_child))
        child.height = 1 + max(self.get_height(child.left_child),
                           self.get_height(child.right_child))

    def _left_rotate(self, node):
        parent = node.parent
        child = node.right_child
        grandchild = child.left_child

        child.left_child = node
        node.parent = child
        node.right_child = grandchild

        if grandchild is not None:
            grandchild.parent = node
        child.parent = parent
        if child.parent is None:
            self.root = child
        else:
            if child.parent.left_child == node:
                child.parent.left_child = child
            else:
                child.parent.right_child = child
        node.height = 1 + max(self.get_height(node.left_child),
                              self.get_height(node.right_child))
        child.height = 1 + max(self.get_height(child.left_child),
                               self.get_height(child.right_child))

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, current_node):
        if current_node is not None:
            self._print_tree(current_node.left_child)
            print("Node data: ", current_node.data, "node height: ", current_node.height)
            self._print_tree(current_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, current_node, current_height):
        if current_node is None:
            return current_height

        left_subtree_height = self._height(current_node.left_child, current_height + 1)
        right_subtree_height = self._height(current_node.right_child, current_height + 1)
        return max(left_subtree_height, right_subtree_height)

    def get_height(self, current_node):
        if current_node is None:
            return 0
        return current_node.height

    def find(self, data):
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, current_node):
        if data == current_node.data:
            return current_node
        elif data < current_node.data and current_node.left_child is not None:
            return self._find(data, current_node.left_child)
        elif data > current_node.data and current_node.right_child is not None:
            return self._find(data, current_node.right_child)

    def more_height_child(self, current_node):
        left_subtree = self.get_height(current_node.left_child)
        right_subtree = self.get_height(current_node.right_child)

        if left_subtree >= right_subtree:
            return current_node.left_child
        else:
            return current_node.right_child


tree = AVLTree()

tree.insert(14)
tree.insert(11)
tree.insert(19)
tree.insert(7)
tree.insert(12)
tree.insert(17)
tree.insert(53)
tree.insert(4)
tree.insert(8)
tree.insert(13)
tree.insert(16)
tree.insert(20)
tree.insert(60)

print(tree)

tree.delete_data(8)
print(tree)
tree.delete_data(7)
print(tree)
tree.delete_data(11)
print(tree)
tree.delete_data(14)
print(tree)
tree.delete_data(17)
print(tree)
