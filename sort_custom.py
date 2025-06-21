from typing import List

#Calculate length of words
def len_words(word: List[str]) -> List[str]:
    return len(word)
        
#Sort words as per length using len_word function as the key
def sort_words(words):
    words.sort(key = len_words, reverse=True) #Descending order
    return words

def abs_nos(num):
    return abs(num)

def sort_nums(nums):
    nums.sort(key = abs_nos, reverse = False)   #Ascending order
    return nums


print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"])) 
print(sort_nums([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))