class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def delete(self, value):
        self.root = self._delete(value, self.root)

    def _delete(self, value, current_node):
        if current_node is None:
            return current_node
        elif value < current_node.value:
            current_node.left = self._delete(value, current_node.left)
        elif value > current_node.value:
            current_node.right = self._delete(value, current_node.right)
        else:
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            current_node.value = self._find_inorder_predecessor(current_node.left)
            current_node.left = self._delete(current_node.value, current_node.left)

        return current_node

    def _find_inorder_predecessor(self, current_node):
        while current_node.right is not None:
            current_node = current_node.right
        return current_node.value

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = TreeNode(value)
            else:
                self._insert(value, current_node.left)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = TreeNode(value)
            else:
                self._insert(value, current_node.right)
        else:
            return None