#1. 

numbers = [10, 20, 30, 40, 50]
print("Sum of the numbers:", sum(numbers))

#2.
numbers = [10, 20, 30, 40, 50]
print("Largest number:", max(numbers))

#3
numbers = [10, 20, 30, 40, 50]
print("Smallest number:", min(numbers))

#4
numbers = [10, 20, 30, 40, 50]
print("Length of the list:", len(numbers))

#5
strings = ["apple", "banana", "cherry", "date", "fig"]
strings.append("grape")
print("Updated list:", strings)

#6
strings = ["apple", "banana", "cherry", "date", "fig"]
strings.insert(2, "grape")  # Insert "grape" at index 2
print("Updated list:", strings)

#7
strings = ["apple", "banana", "cherry", "date", "fig"]
popped_word = strings.pop(3)  # Remove the word at index 3
print("Popped word:", popped_word)
print("Updated list:", strings)