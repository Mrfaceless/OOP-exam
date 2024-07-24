from queue import PriorityQueue
p = PriorityQueue()
p.put((3, 'yashashwa'))  
p.put((1, 'hello'))  
p.put((2, 'I am'))
print("Popped elements in order of priority:")
while not p.empty():
    priority, data = p.get()
    print(f'Priority: {priority}, Data: {data}')
if p.empty():
    print("Priority queue is empty")
else:
    print("Priority queue is not empty")
