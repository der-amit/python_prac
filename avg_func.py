def avg_function(*values):
    average = sum(values) / len(values)
    return round(average,2)

inp = input("Enter numbers separated by commas: ")

numbers = [float(x.strip()) for x in inp.split(',')]
print(avg_function(*numbers))