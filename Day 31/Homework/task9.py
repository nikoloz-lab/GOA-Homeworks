def find_index(my_list, number):
    if number in my_list:
        print(my_list.index(number))
    else:
        print(f"{number} is not in the list.")