import time

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left:
                self._insert(node.left, key)
            else:
                node.left = Node(key)
        else:
            if node.right:
                self._insert(node.right, key)
            else:
                node.right = Node(key)

    def inorder(self, node):
        return self.inorder(node.left) + [node.key] + self.inorder(node.right) if node else []
    
    def preorder(self, node):
        return [node.key] + self.preorder(node.left) + self.preorder(node.right) if node else []
    
    def postorder(self, node):
        return self.postorder(node.left) + self.postorder(node.right) + [node.key] if node else []

start_time = time.time()
bst = BST()
for num in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(num)

print("In-order:", bst.inorder(bst.root))
print("Pre-order:", bst.preorder(bst.root))
print("Post-order:", bst.postorder(bst.root))
print("Tempo de execução:", time.time() - start_time, "segundos")
