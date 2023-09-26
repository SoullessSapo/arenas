class Node:
def __init__(self, key):
        self.key = key
        self.left = None
        self.rigt = None
        self.balance_factor = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def _update_balance_factor(self, node):
        # Función interna para actualizar el factor de balance AVL de un nodo
        if node is None:
            return 0
        left_height = self._update_balance_factor(node.left)
        right_height = self._update_balance_factor(node.right)
        node.balance_factor = right_height - left_height
        return max(left_height, right_height) + 1

    def _rotate_left(self, z):
        # Rotación izquierda en caso de desbalanceo
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self._update_balance_factor(z)
        self._update_balance_factor(y)
        return y

    def _rotate_right(self, y):
        # Rotación derecha en caso de desbalanceo
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        self._update_balance_factor(y)
        self._update_balance_factor(x)
        return x

    def _rebalance(self, node):
        # Rebalancea el árbol a partir de un nodo
        if node.balance_factor < -1:  # Desbalance a la izquierda
            if node.left.balance_factor > 0:  # Desbalance en zigzag izquierda-derecha
                node.left = self._rotate_left(node.left)
            node = self._rotate_right(node)
        elif node.balance_factor > 1:  # Desbalance a la derecha
            if node.right.balance_factor < 0:  # Desbalance en zigzag derecha-izquierda
                node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
        return node

    def insert(self, key):
        self.root = self._insert(key, self.root)

    def _insert(self, key, node):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(key, node.left)
        elif key > node.key:
            node.right = self._insert(key, node.right)
        else:
            # Clave ya existente, no se permite duplicados
            return node

        # Actualizar el factor de balance AVL del nodo
        self._update_balance_factor(node)

        # Rebalancear el árbol si es necesario
        node = self._rebalance(node)

        return node

    def delete(self, key):
        self.root = self._delete(key, self.root)

    def _delete(self, key, node):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(key, node.left)
        elif key > node.key:
            node.right = self._delete(key, node.right)
        else:
            # Encontrado el nodo a eliminar
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
    .
    00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000121
1
def main():
    # Crear un árbol binario de búsqueda con factor de balance AVL
    bst = BinarySearchTree()

    # Insertar elementos en el árbol
    elements_to_insert = [10, 20, 30, 40, 50, 60, 70]
    print("Insertando elementos en el árbol:")
    for elem in elements_to_insert:
        bst.insert(elem)
        print(f"Elemento {elem} insertado.")

    # Eliminar un elemento del árbol
    element_to_delete = 30
    print(f"\nEliminando el elemento {element_to_delete} del árbol:")
    bst.delete(element_to_delete)
    print(f"Elemento {element_to_delete} eliminado.")

    # Mostrar el árbol inorden
    print("\nÁrbol inorden:")
    bst.inorder_traversal()

    # Mostrar el árbol preorden
    print("\nÁrbol preorden:")
    bst.preorder_traversal()

    # Mostrar el árbol postorden
    print("\nÁrbol postorden:")
    bst.postorder_traversal()

if __name__ == "__main__":
    main()