
'''
The inner list is a reference to the same list object. 
This means that if we change one of the inner lists, all the inner lists will change
'''
grid = [[0] * 3] * 2
print(grid)

grid[0][1] = 1
print(grid) 

'''
A better way to initialize a 2-D list is to use a nested list comprehension:

'''
