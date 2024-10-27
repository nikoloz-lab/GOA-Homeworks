#შექმენით 1 ლისტი და გამოიყენეთ ყველა ფუნქცია რაც დღეს გავიარეთ

sheet = pd.DataFrame(columns=['A', 'B', 'C', 'D', 'E'])

sheet.loc[0, 'B'] = 'Variable in 2nd place'
sheet.loc[0, 'E'] = 'Variable in 5th place'

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

removed_from_list1 = [list1.pop(), list1.pop()]
removed_from_list2 = [list2.pop(), list2.pop()]

sheet.loc[0, 'C'] = removed_from_list1[0]
sheet.loc[0, 'D'] = removed_from_list2[0]

print("Final Sheet:")
print(sheet)
print("\nModified List 1:", list1)
print("Modified List 2:", list2)
