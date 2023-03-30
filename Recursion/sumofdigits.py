def sumofdigits(num):
    assert num >= 0 and isinstance(num, int), 'Incorrect number'
    if num == 0:
        return 0
    else:
        if (int(num%10) + int(sumofdigits(num//10))) < 10:
            return int(num%10) + int(sumofdigits(num//10))
        else:
            return sumofdigits(int(num%10) + int(sumofdigits(num//10)))

a = [1,2,4,3,6,9]
b = sorted(a)[-1]
print(b)
# print(sorted([1,3,5,2,11,9])[0])