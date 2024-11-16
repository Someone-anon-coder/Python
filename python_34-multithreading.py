import threading
import time

def worker(num: int) -> None:
    print(f"Worker {num} started")
    time.sleep(2)
    print(f"After 2 seconds, Worker {num} finished")

threads = []

for i in range(4):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads finished")


def worker(lock: threading.Lock, shared_data: dict) -> None:
    with lock:
        shared_data['counter'] += 1
        print(f"Counter Value: {shared_data['counter']}")

lock = threading.Lock()
shared_data = {'counter': 0}
threads = []

for _ in range(5):
    thread = threading.Thread(target=worker, args=(lock, shared_data))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(f"Final Counter Value: {shared_data['counter']}")


def worker(event: threading.Event) -> None:
    print("Worker started")
    event.wait()
    print("Worker finished")

event = threading.Event()
threads = []

for _ in range(3):
    thread = threading.Thread(target=worker, args=(event,))
    threads.append(thread)
    thread.start()

time.sleep(2)
event.set()

for thread in threads:
    thread.join()

print("All threads finished")


from concurrent.futures import ThreadPoolExecutor

def square(num: int) -> int:
    return num * num

with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(square, [1, 2, 3, 4, 5])
    print("Squares:", list(results))