print("Hello World")

a = 10
b = 20
print(a + b)

str1 = "Hello"
str2 = "World"
print(str1 + str2)  # Output: HelloWorld

x = 10
y = 4
print(x / y)  # Output: 2.5

print(5 == 5)  # True
print(10 != 5)  # True
print(7 > 3)  # True
print(2 < 4)  # True
print(6 >= 6)  # True
print(9 <= 10)  # True

print(5 + 5 == 8 + 2)  # True
print(10 - 3 > 4 + 2)  # True

print(True and True)  # True
print(True and False)  # False
print(False or True)  # True
print(not True)  # False

print(5 > 3 and 10 < 20)  # True
print(7 == 7 or 2 > 5)  # True
print(not (4 <= 5))  # False
print((6 > 3) and (8 == 8))  # True
print((5 + 2 > 10) or (3 + 3 == 6))  # True

for i in range(1, 11):
    print(i)

string = "Hello, World!"
for char in string:
    print(char)

i = 1
while i <= 10:
    print(i)
    i += 1

total = 0
i = 1
while total < 50:
    total += i
    i += 1
print(total)  # Output: 50

def arithmetic_mean(numbers):
    return sum(numbers) / len(numbers)

print(arithmetic_mean([1, 3, 4, 5, 2]))  # Output: 3

def square_numbers(numbers):
    squared_list = [x ** 2 for x in numbers]
    return squared_list

print(square_numbers([3, 12, 5, 2, 6]))  # Output: [9, 144, 25, 4, 36]

my_list = [1, 2, 3, 4]
my_list.append(5)  
print(my_list)  # [1, 2, 3, 4, 5]

my_list.pop()  
print(my_list)  # [1, 2, 3, 4]

my_list.sort(reverse=True) 
print(my_list)  # [4, 3, 2, 1]

my_string = "hello world"
print(my_string.upper())  
print(my_string.replace("world", "Python"))  
print(my_string.split()) 