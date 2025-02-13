import numpy as np
import multiprocessing
import time

def multiply_row(args):
    row, matrix_b = args
    return [sum(a * b for a, b in zip(row, col)) for col in zip(*matrix_b)]

def parallel_matrix_multiplication(matrix_a, matrix_b):
    with multiprocessing.Pool() as pool:
        result = pool.map(multiply_row, [(row, matrix_b) for row in matrix_a])
    return result

if __name__ == "__main__":
    matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
    
    start_time = time.time()
    result_matrix = parallel_matrix_multiplication(matrix_a, matrix_b)
    end_time = time.time()
    
    for row in result_matrix:
        print(row)
    
    print("Tempo de execução:", end_time - start_time)
