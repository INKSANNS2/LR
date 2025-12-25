import time
class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        elapsed = self.end_time - self.start_time
        print(f"Время выполнения: {elapsed:.2f} сек")
        return False
with Timer():
    time.sleep(1.5)
print("\nТест с ошибкой:")
try:
    with Timer():
        time.sleep(0.5)
        raise ValueError("чернобыль")
except ValueError as e:
    print(f"Поймали ошибку: {e}")