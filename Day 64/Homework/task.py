#1. https://www.codewars.com/kata/5b853229cfde412a470000d0/train/python

def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)

#2. https://www.codewars.com/kata/55d24f55d7dd296eb9000030/train/python

def summation(num):
    return sum(range(1, num + 1))

#3. https://www.codewars.com/kata/5861d28f124b35723e00005e/train/python

def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump

#4. https://www.codewars.com/kata/5bb0c58f484fcd170700063d/train/python

def pillars(num_pill, dist, width):
    if num_pill == 1:
        return 0
    return (num_pill - 1) * dist * 100 + (num_pill - 2) * width

#5. https://www.codewars.com/kata/59342039eb450e39970000a6/train/python

def odd_count(n):
    return n // 2
