import time
import multiprocessing

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def count_primes_in_range(start, end):
    return sum(1 for i in range(start, end) if is_prime(i))

def sequential_prime_count(n):
    return count_primes_in_range(1, n)

def parallel_prime_count(n):
    num_workers = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_workers)
    step = n // num_workers
    ranges = [(i, min(i + step, n)) for i in range(1, n, step)]
    result = sum(pool.starmap(count_primes_in_range, ranges))
    pool.close()
    pool.join()
    return result

n = 100000
start_time = time.time()
seq_result = sequential_prime_count(n)
seq_time = time.time() - start_time

start_time = time.time()
par_result = parallel_prime_count(n)
par_time = time.time() - start_time

print(f"Contagem de primos (sequencial): {seq_result}, Tempo: {seq_time:.4f} segundos")
print(f"Contagem de primos (paralela): {par_result}, Tempo: {par_time:.4f} segundos")
