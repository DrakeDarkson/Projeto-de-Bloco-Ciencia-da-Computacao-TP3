import multiprocessing
import time

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_primes_in_range(start, end):
    return sum(1 for n in range(start, end) if is_prime(n))

def parallel_prime_count(start, end, num_workers):
    step = (end - start) // num_workers
    ranges = [(start + i * step, start + (i + 1) * step) for i in range(num_workers)]
    ranges[-1] = (ranges[-1][0], end)
    
    with multiprocessing.Pool(num_workers) as pool:
        results = pool.starmap(count_primes_in_range, ranges)
    
    return sum(results)

if __name__ == "__main__":
    start_time = time.time()
    num_workers = multiprocessing.cpu_count()
    prime_count = parallel_prime_count(1, 100000, num_workers)
    end_time = time.time()
    
    print(f"Número total de primos entre 1 e 100000: {prime_count}")
    print(f"Tempo total de execução: {end_time - start_time:.4f} segundos")