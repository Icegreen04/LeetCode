'''
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.
Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
'''
def RunningSum():
    nums=[2,3,5,6,10,20,22]
    i=1
    n=len(nums)
    while i<n:
        nums[i]=nums[i]+nums[i-1]
        i+=1
    return nums
print(RunningSum())
'''
this is a slower but a more conventionally expected solution
n=len(nums)
        arr=[0]*n
        arr[0]=nums[0]
        i=1
        while i<n:
            arr[i]=arr[i-1]+nums[i]
            i+=1
        return arr
'''