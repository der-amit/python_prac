nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


'''
Printing all elements in the list
'''

for s in nested_list:
    for i in s:
        print(i)

'''
===Find the max element in each list===
Expected output:

[2, 4]
[3, 6, 9]
[8, 9, 10, 11]

'''

def get_max(nested_list):
    mylist = []
    for sublist in nested_list:
        #print(sublist)
        mylist.append(max(sublist))
    return mylist
    
    
print(get_max([[1, 2], [3, 4, 2]]))
print(get_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(get_max([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))


            
