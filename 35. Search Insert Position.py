'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''
def SearchInsertPos():
    nums=[2,3,5,6,7,8,9,11,14,15,16,22,24,25]
    target=23
    left=0
    right=len(nums)-1
    while left<=right:
        mid=(left+right)//2
        if target==nums[mid]:
            return mid
        elif nums[mid]<target:
            left=mid+1
        else:
            right=mid-1
    else:
        return left
print(SearchInsertPos())