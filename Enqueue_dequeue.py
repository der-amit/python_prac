from collections import deque

queue = deque()

for k in range(5):
    queue.append(k)
    print(queue) 
queue.popleft()
print(queue)

'''
===Rotate by k Steps===
'''

def rotate_list(arr, k):
    q = deque(arr)
    for n in range(k):
        q.append(q.popleft())
    return q

print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))

'''
=== Double Ended Queue ===
'''

def rotate_list(arr, k):
    q = deque(arr)
    for i in range(k):
        q.appendleft(q.pop())
    return q

# do not modify below this line
print(rotate_list([1, 2, 3, 4, 5], 0))
print(rotate_list([1, 2, 3, 4, 5], 1))
print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 3))
print(rotate_list([1, 2, 3, 4, 5], 4))
print(rotate_list([1, 2, 3, 4, 5], 5))