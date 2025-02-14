import threading
import time

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def find_max_parallel(root):
    if root is None:
        return float('-inf')
    
    max_value = root.value
    left_max = right_max = float('-inf')
    
    def search_left():
        nonlocal left_max
        left_max = find_max_parallel(root.left)
    
    def search_right():
        nonlocal right_max
        right_max = find_max_parallel(root.right)
    
    left_thread = threading.Thread(target=search_left)
    right_thread = threading.Thread(target=search_right)
    
    left_thread.start()
    right_thread.start()
    
    left_thread.join()
    right_thread.join()
    
    return max(max_value, left_max, right_max)

root = None
values = [15, 10, 20, 8, 12, 17, 25]
for v in values:
    root = insert(root, v)

start_time = time.time()
max_value = find_max_parallel(root)
end_time = time.time()

print("Valor máximo encontrado:", max_value)
print("Tempo total de execução:", end_time - start_time, "segundos")
