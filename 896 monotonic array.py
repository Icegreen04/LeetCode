'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.

 

Example 1:

Input: nums = [1,2,2,3]
Output: true
'''
def monotonic():   
    nums=[2,3,4,5,5,6]
    if len(nums) <= 1:
        return True
            
    change = 0
    if nums[0] < nums[-1]:
        change = 1
    else:
        change = 2

    if change == 1:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return False
    else:
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                return False

    return True

print(monotonic())