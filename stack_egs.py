'''===REVERSE OF A LIST==='''

def reverse_list(arr):
    rev_list = []
    while len(arr) > 0:
        rev_list.append(arr.pop())
    return rev_list
        

print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
