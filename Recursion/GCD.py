def findGCDlst(nums):
    a = sorted(nums)[-1]
    b = sorted(nums)[0]
    def findGCD(x,y):
        if x < 0:
            x = -1 * x
        if y < 0:
            y = -1 * y
        if y == 0:
            return x
        else:
            return findGCD(y, x % y)
    return findGCD(a,b)


print(findGCDlst([2,5,6,9,10]))