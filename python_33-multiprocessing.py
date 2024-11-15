import multiprocessing
import time

def worker(num: int) -> None:
    print(f"Worker {num} started")
    
    time.sleep(2)

    print(f"After 2 seconds, Worker {num} finished")

processes = []

for i in range(4):
    process = multiprocessing.Process(target=worker, args=(i,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

print("All processes finished")


def worker(queue: multiprocessing.Queue, num: int) -> None:
    result = num * num
    queue.put(result)

queue = multiprocessing.Queue()

processes = []

for i in range(4):
    process = multiprocessing.Process(target=worker, args=(queue, i))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

while not queue.empty():
    print("Result:", queue.get())

print("All processes finished")


def square(num: int) -> int:
    return num * num

with multiprocessing.Pool(processes=4) as pool:
    results = pool.map(square, [1, 2, 3, 4, 5])

print("Sqaures:", results)


def worker(lock: multiprocessing, shared_data: dict) -> None:
    with lock:
        for _ in range(5):
            shared_data['counter'] += 1
            print(f"Counter Value: {shared_data['counter']}")
            time.sleep(0.1)

manager = multiprocessing.Manager()
shared_data = manager.dict({'counter': 0})

lock = multiprocessing.Lock()
processes = []

for _ in range(3):
    process = multiprocessing.Process(target=worker, args=(lock, shared_data))
    processes.append(process)
    process.start()

for process in processes:
    process.join()

print(f"Final Counter Value: {shared_data['counter']}")