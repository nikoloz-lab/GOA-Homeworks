numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num / 2 == 0:
     print(num + 2)

#bonus

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_odd = sum(num for num in numbers if num / 2 != 0)
sum_even =sum(num for num in numbers if num / 2 == 0)

result = sum_odd - sum_even
print(result)