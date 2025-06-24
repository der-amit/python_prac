from typing import List


def sort_words(words: List[str]) -> List[str]:
    sorted_list  = sorted(words, reverse = False)
    return sorted_list

def sort_numbers(numbers: List[int]) -> List[int]:
    sorted_nums = sorted(numbers, key = abs, reverse = True)
    return sorted_nums

# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)
print(sort_words(original_words))

original_numbers = [1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]

print(original_numbers)
print(sort_numbers(original_numbers))
