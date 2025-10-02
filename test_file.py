from collections import deque

queue = deque([1,2,3,4,5,5,6])
'''queue.append(1)
queue.append(2)

queue.append(4)
'''
for k in list(queue):
    if k%2 == 0:
        queue.remove(k)
    print(queue)

