def find_it(seq):
    """
    Given an array of integers, find the one that appears an odd number of times.
    
    There will always be only one integer that appears an odd number of times.
    """
    # Use a dictionary to count occurrences of each number
    count_dict = {}
    
    # Count the occurrences of each number
    for num in seq:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Find the number with an odd count
    for num, count in count_dict.items():
        if count % 2 == 1:  # Check if count is odd
            return num
    
    # Alternative one-liner using collections.Counter
    # from collections import Counter
    # return [num for num, count in Counter(seq).items() if count % 2 == 1][0]