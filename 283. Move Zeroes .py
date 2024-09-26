'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

'''
def MoveZero():
    nums=[1,2,0,0,4,3,2,4,0,8,6,0]
    last_non_zero=0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1
        print(nums)

    for i in range(last_non_zero, len(nums)):
        nums[i] = 0
        print(nums)
    return nums
print(MoveZero())