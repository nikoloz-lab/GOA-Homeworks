# შექმენით ფუნქცია, სადაც გექნებათ 5 სიტყვიანი სია, შემდეგ მომხმარებელს შემოატანინეთ 0-იდან 5-მდე რიცხვი, და დაუპრინტეთ ეგ index თქვენი შექმნილი სიიდან.3

def print_word_from_list():
   
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    
    try:
        index = int(input("Enter a number between 0 and 4: "))
        if 0 <= index <= 4:
            print(f"The word at index {index} is: {words[index]}")
        else:
            print("Error: Number out of range. Please enter a number between 0 and 4.")
    except ValueError:
        print("Error: Invalid input. Please enter an integer.")


print_word_from_list()