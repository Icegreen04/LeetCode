'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3

'''
def MajElementArr():
    nums=[2,2,1,4,5,6,7,6,5,4,4,4,4,3,2]
    maj=1
    majele=nums[0]
    for i in range(1,len(nums)):
        if maj==0:
            majele=nums[i]
        if nums[i]==majele:
            maj+=1
        else:
            maj-=1
    return majele
print(MajElementArr())