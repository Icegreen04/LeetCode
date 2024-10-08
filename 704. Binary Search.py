'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
'''
def BinSearch(nums,target):
    left=0
    right=len(nums)-1
    mid=(right+left)//2
    while True:
        if nums[mid]==target:
            return mid
        mid=(right+left)//2
        if nums[mid]==target:
            return mid
        elif left==right or right<left:
            return -1
        elif nums[mid]<target:
            left=mid+1
        elif nums[mid]>target:
            right=mid-1
        else:
            return -1
nums=[-20,-18,0,3,4,20,22,44,100,180]
target=-17
print(BinSearch(nums,target))