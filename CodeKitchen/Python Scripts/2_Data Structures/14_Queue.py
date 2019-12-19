from collections import deque

# we don't use list to implement queue here , as it not as efficient. (shifting all element in queue.)
# hence we wrap list in deque object  which provides special methods to acesss data.

queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)

# Empty Queue.
if not queue:
    print("Empty Queue.")
