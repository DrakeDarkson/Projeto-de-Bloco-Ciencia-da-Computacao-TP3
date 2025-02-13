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

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)

def main():
    start_time = time.time()
    bst = BST()
    elements = [50, 30, 70, 20, 40, 60, 80]
    for el in elements:
        bst.insert(el)
    
    search_value = 40
    found = bst.search(search_value)
    print(f'Elemento {search_value} encontrado: {found}')
    
    end_time = time.time()
    print(f'Tempo total de execução: {end_time - start_time:.6f} segundos')

if __name__ == "__main__":
    main()