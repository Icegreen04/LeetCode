'''
You are given two arrays of equal length, nums1 and nums2.

Each element in nums1 has been increased (or decreased in the case of negative) by an integer, represented by the variable x.

As a result, nums1 becomes equal to nums2. Two arrays are considered equal when they contain the same integers with the same frequencies.
Return the integer x.
Example 1:

Input: nums1 = [2,6,4], nums2 = [9,7,5]

Output: 3

Explanation:

The integer added to each element of nums1 is 3.
'''
def IntAddArray():
    nums1=[5,4,2]
    nums2=[8,6,9]
    n1=max(nums1)
    n2=max(nums2)
    return n2-n1
print(IntAddArray())
'''
ONE MORE METHOD USING SUMS AND THEN DIVIDING
n=len(nums1)
        n1=sum(nums1)
        n2=sum(nums2)
        return int((n2-n1)/n)
'''