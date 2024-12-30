#1. https://www.codewars.com/kata/524f5125ad9c12894e00003f


def remainder(n, m):
    if m == 0 or n == 0:
       return float ('Nan')
    return max (n, m) % min(n, m)

#მაგალითი =)
print(remainder(17, 5)) #პასუხი:2
print(remainder(13, 72)) #პასუხი:13
print(remainder(0, -1)) #პასუხი: NaN
print(remainder(0, 1)) #პასუხი: NaN