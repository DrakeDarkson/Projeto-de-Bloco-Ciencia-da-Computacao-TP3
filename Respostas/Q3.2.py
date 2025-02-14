import time
import threading

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def dfs_parallel(node, target, path, result, lock):
    if node is None:
        return False
    
    path.append(node.key)
    
    if node.key == target:
        with lock:
            result.extend(path)
        return True
    
    left_result = [None]
    right_result = [None]
    left_thread = threading.Thread(target=lambda: left_result.__setitem__(0, dfs_parallel(node.left, target, path[:], result, lock)))
    right_thread = threading.Thread(target=lambda: right_result.__setitem__(0, dfs_parallel(node.right, target, path[:], result, lock)))
    
    left_thread.start()
    right_thread.start()
    left_thread.join()
    right_thread.join()
    
    return left_result[0] or right_result[0]

def find_path(root, target):
    result = []
    lock = threading.Lock()
    dfs_parallel(root, target, [], result, lock)
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

target = 5
start_time = time.time()
path = find_path(root, target)
end_time = time.time()

print("Caminho encontrado:", path)
print("Tempo total de execução:", end_time - start_time, "segundos")
