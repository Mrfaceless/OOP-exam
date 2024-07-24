import queue

q = queue.Queue()

q.put('hi')
q.put('i am')
q.put('yashashwa')

print("Queue with new elements:")
print(list(q.queue))

removed_element = q.get() #as queue from import does not have .pop() method

print("Removed element:", removed_element)

print("Queue after removing an element:")
print(list(q.queue))
