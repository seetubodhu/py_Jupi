from collections import deque


queue =["Eric", "John", "Michael"]
print(queue)
queue.append("Terry")           # Terry arrives
print(queue)
queue.append("Graham")          # Graham arrives
print(queue)
queue.pop(0)                 # The first to arrive now leaves
print(queue)
queue.pop(0)                 # The second to arrive now leaves
print(queue)
x = deque(['Michael', 'Terry', 'Graham'])
print(x)