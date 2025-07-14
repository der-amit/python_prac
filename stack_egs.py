'''===REVERSE OF A LIST==='''
'''
Implement the following function using the stack operations described above:

reverse_list(arr: List[int]) -> List[int] that takes a list of integers and returns a new list of the integers in reverse order.
Hint: Recall that elements from a stack are removed in reverse order.
'''
def reverse_list(arr):
    rev_list = []
    while len(arr) > 0:
        for k in arr:
            rev_list.append(arr.pop())
    return rev_list
        

print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
