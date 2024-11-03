stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(f"Stack: {stack}")

print(f"Removing the top most element: {stack.pop()}")

print(f"Peeking at the top element: {stack[-1]}")


from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

print(f"Queue: {queue}")

print(f"Removing the first element: {queue.popleft()}")

print(f"Peeking at the first element: {queue[0]}")