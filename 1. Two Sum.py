'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
def twoSum(nums,target):
    target_set={}
    for i in range(len(nums)):
        if nums[i] in target_set:
            return [target_set[nums[i]],i]
        else:
            target_set[target-nums[i]]=i

target=10
nums=[2,4,5,6,7,9]
print(twoSum(nums,target))