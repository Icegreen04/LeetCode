'''
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
'''
def validPerfSquare():
    num=100
    if num==1:
        return True
    left=1
    right=num//2
    while left<=right:
        mid=(left+right)//2
        temproot=mid*mid
        if temproot==num:
            return True
        elif temproot<num:
            left=mid+1
        else:
            right=mid-1
    else:
        return False
print(validPerfSquare())