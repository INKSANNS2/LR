def fibonacci(n):
    if n <= 1:   
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def tail_fibonacci(n, current=0, next_num=1):
    if n == 0:             
        return current
    elif n == 1:              
        return next_num
    else:

        return tail_fibonacci(n - 1, next_num, current + next_num)
    
import time

n = 35

# Замер обычной рекурсии
start_time = time.time()
print(f"Fibonacci({n}) = {fibonacci(n)}")
print(f"Time taken (Naive): {time.time() - start_time:.6f} seconds")

# Замер хвостовой рекурсии
start_time = time.time()
print(f"Tail Fibonacci({n}) = {tail_fibonacci(n)}")
print(f"Time taken (Tail): {time.time() - start_time:.6f} seconds")