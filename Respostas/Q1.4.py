import time

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert(node.right, value)

    def is_valid_bst(self):
        return self._is_valid_bst(self.root, float('-inf'), float('inf'))

    def _is_valid_bst(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return (self._is_valid_bst(node.left, min_val, node.value) and
                self._is_valid_bst(node.right, node.value, max_val))

def main():
    start_time = time.time()
    bst = BST()
    elements = [50, 30, 70, 20, 40, 60, 80]
    for el in elements:
        bst.insert(el)
    
    print(f'É uma BST válida: {bst.is_valid_bst()}')
    
    bst.root.left.right.value = 100
    print(f'É uma BST válida após modificação: {bst.is_valid_bst()}')
    
    end_time = time.time()
    print(f'Tempo total de execução: {end_time - start_time:.6f} segundos')

if __name__ == "__main__":
    main()
