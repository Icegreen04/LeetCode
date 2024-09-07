'''
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.

 

Example 1:

Input: nums = [1,15,6,3]
Output: 9
Explanation: 
The element sum of nums is 1 + 15 + 6 + 3 = 25.
The digit sum of nums is 1 + 1 + 5 + 6 + 3 = 16.
The absolute difference between the element sum and digit sum is |25 - 16| = 9.
'''
def DiffInSums():
    nums=[30,2,4,5,100,23]
    elesum=sum(nums)
    digitsum=0
    for i in range(len(nums)):
        store=nums[i]
        while store>0:
            digitsum+=store%10
            store=store/10
            store=int(store)
    elesum=elesum-digitsum
    if elesum<0:
        elesum=elesum*-1
    return elesum
print(DiffInSums())
