import time
import threading

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def parallel_search(self, value):
        result = [False]
        threads = []
        
        def search_subtree(node):
            if node is None:
                return
            if node.key == value:
                result[0] = True
            else:
                search_subtree(node.left)
                search_subtree(node.right)
        
        if self.root:
            if self.root.key == value:
                return True
            
            if self.root.left:
                t1 = threading.Thread(target=search_subtree, args=(self.root.left,))
                threads.append(t1)
                t1.start()
            
            if self.root.right:
                t2 = threading.Thread(target=search_subtree, args=(self.root.right,))
                threads.append(t2)
                t2.start()
            
            for t in threads:
                t.join()
        
        return result[0]

bt = BinaryTree()
for value in [50, 30, 70, 20, 40, 60, 80]:
    bt.insert(value)

start_time = time.time()
found = bt.parallel_search(60)
end_time = time.time()

time_taken = end_time - start_time
print(f"Elemento 60 {'encontrado' if found else 'não encontrado'}")
print(f"Tempo total de execução: {time_taken:.6f} segundos")
