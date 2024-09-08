'''
You are given an integer array nums (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

For example, if nums = [1,2,3], you can choose to increment nums[1] to make nums = [1,3,3].
Return the minimum number of operations needed to make nums strictly increasing.

An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. An array of length 1 is trivially strictly increasing.

 

Example 1:

Input: nums = [1,1,1]
Output: 3
Explanation: You can do the following operations:
1) Increment nums[2], so nums becomes [1,1,2].
2) Increment nums[1], so nums becomes [1,2,2].
3) Increment nums[2], so nums becomes [1,2,3].
'''
def IncreasingArrMin():
    nums=[2,1,40,5,3,2]
    count=0
    n=len(nums)
    i=1
    while i < n:
        if nums[i]<=nums[i-1]:
            count+=nums[i-1]-nums[i]+1
            nums[i]=nums[i-1]+1
            i+=1
        else:
            i+=1
    return count
print(IncreasingArrMin())