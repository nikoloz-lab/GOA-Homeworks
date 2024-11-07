# Task 1: 
list1 = [10, 20, 30, 40, 50]
list2 = [5, 15, 25, 35, 45]
list3 = [7, 17, 27, 37, 47]

print("Maximum of list1:", max(list1))
print("Maximum of list2:", max(list2))
print("Maximum of list3:", max(list3))

# Task 2: 
print("\nMinimum of list1:", min(list1))
print("Minimum of list2:", min(list2))
print("Minimum of list3:", min(list3))

# Task 3: 
print("\nLength of list1:", len(list1))
print("Length of list2:", len(list2))
print("Length of list3:", len(list3))

# Task 4: 
list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list5 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list6 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
list7 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

# 1) 
print("\nFirst to fourth element of list4:", list4[:4])

# 2) 
print("\nFourth to eighth element of list5:")
for i in range(3, 8):
    print(list5[i], end=" ")

# 3) 
print("\n\nNinth to sixth element of list6 in reverse order:", list6[8:5:-1])

# 4) 
print("\nAll elements of list7 using while loop:")
i = 0
while i < len(list7):
    print(list7[i], end=" ")
    i += 1
