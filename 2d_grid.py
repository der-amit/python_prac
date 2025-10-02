grid = [
    [1,2,3],
    [0,0,0]
]

rows = len(grid)
cols = len(grid[0])

print(f'Rows are: {rows}\nColumns are: {cols}')

'''
in_bounds(grid: List[int], r: int, c: int) -> bool that takes a 2D grid grid and two integers r and c, 
where r is the index of a row and c is the index of a column. 
It should return True if the cell at row r and column c is within the bounds of the grid, and False otherwise.
Example: in_bounds([[1, 2], [3, 4]], 2, 1) should return False, there is no row at index 2.
'''

def in_bounds(grid, r,c):
    if ((r > len(grid)-1) or (r < -len(grid))) or ((c > len(grid[0])-1) or (c< -len(grid[0]))):
        return False
    else:
        return True



print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0, 0))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2, 2))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1, 1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4, 3))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, 4))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 3, -1))
print(in_bounds([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1, 3))