#Lambda function with 1 argument to perform average

avg = (lambda x: sum(x)/len(x))
print(avg([2,3,4]))

#Lambda function with 2 arguments to perform multiplication

multiply = (lambda a,b: a*b)
print(multiply(2,4))

#Lambda function with iterables :apply lambda inside map()
names = ["mo", "bobby", "sadio"]
caps = map(lambda k: k.capitalize(), names)

#Convert to a list and print
print(list(caps))