#Eg: Lambda function with 1 argument to perform average

avg = (lambda x: sum(x)/len(x))
print(avg([2,3,4]))

#Eg: Lambda function with 2 arguments to perform multiplication

multiply = (lambda a,b: a*b)
print(multiply(2,4))

#Eg: Lambda function with iterables :apply lambda inside map()
names = ["mo", "bobby", "sadio"]
caps = map(lambda k: k.capitalize(), names)

#Convert to a list and print
print(list(caps))            

#EGa.1: Another iterable example using map function
sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

add_taxes = map(lambda price: price*1.2, sales_prices)
sales_plus_tax = list(add_taxes)
print(sales_plus_tax)

#EGa.2: Getting the same result with a more pythonic way

add_tax = lambda x: x*1.2
with_tax = list(add_tax(k) for k in sales_prices)
print(with_tax)

