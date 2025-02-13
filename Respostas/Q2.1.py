import multiprocessing
import time

def partial_sum(numbers):
    return sum(numbers)

def parallel_sum(n):
    num_cores = multiprocessing.cpu_count()
    chunk_size = n // num_cores
    numbers = list(range(1, n + 1))
    
    with multiprocessing.Pool(processes=num_cores) as pool:
        chunks = [numbers[i * chunk_size:(i + 1) * chunk_size] for i in range(num_cores)]
        results = pool.map(partial_sum, chunks)
    
    return sum(results)

if __name__ == "__main__":
    start_time = time.time()
    result = parallel_sum(10_000_000)
    end_time = time.time()
    
    print(f"Soma total: {result}")
    print(f"Tempo de execução: {end_time - start_time:.4f} segundos")
