#A function to return the location of a number
def get_index(nums):
    for i, n in enumerate(nums):
        if n==7:
            return i
    return -1       # -1 -> number does not exist in the list

#A function to calculate the first and second occurence of a number    
def dist_between_sevens(nums):
    loc_first_seven = -1
    for i, n in enumerate(nums):
        if n == 7:
            if loc_first_seven == -1:
                loc_first_seven = i
            else:
                return i - loc_first_seven
        #return -1
        
    
print(get_index([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(get_index([1, 2, 3, 4, 5, 6, 8, 9]))
print(get_index([2, 4, 7, 5, 7, 8, 4, 2]))

print(dist_between_sevens([1, 2, 7, 4, 5, 6, 7, 8, 9]))
print(dist_between_sevens([2, 7, 7, 7, 8]))
print(dist_between_sevens([7, 4, 8, 4, 2, 7]))