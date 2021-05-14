from functools import reduce

numbers = [1,3,5,7,9]

def sum_num(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    print(total)

sum_num(numbers)

def add(x, y):
    return(x+y)

def subtract(x, y):
    return(x-y)

print(reduce(add, numbers))

def calculate(operation, x, y):
    return operation(x,y)
    
print(calculate(add, 3, 5))

print(calculate(subtract, 3, 5))

new_list = []

for i in range(len(numbers)):
    if numbers[i] >= 5:
        new_list.append(numbers[i])
print(new_list)    

def overFive(num):
    return True if num >= 5 else False

print(list(filter(overFive, numbers)))
