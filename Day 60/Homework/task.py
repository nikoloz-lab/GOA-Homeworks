#1. https://www.codewars.com/kata/577a98a6ae28071780000989/train/python

def min_max(lst):
    return [min(lst), max(lst)]

#2. https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python

def area_or_perimeter(l, w):
    if l == w:
        return l * w  
    else:
        return 2 * (l + w) 

#3. https://www.codewars.com/kata/58261acb22be6e2ed800003a/train/python

def get_volume_of_cuboid(length, width, height):
    return length * width * height

#4. https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

def count_positives_sum_negatives(arr):
    count = len([x for x in arr if x > 0])  # Count positive numbers
    total = sum(x for x in arr if x < 0)    # Sum negative numbers
    return [count, total]

#5. https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python

def check(seq, elem):
    return elem in seq