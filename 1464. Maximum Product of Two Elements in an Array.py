'''
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
'''
def twolargest():
    nums=[3,4,2,5,5,22,3,11]
    largest=secondlargest=float('-inf')
    for i in nums:
        if i>largest:
            secondlargest=largest
            largest=i
        elif i>secondlargest:
            secondlargest=i
    return (largest-1)*(secondlargest-1)
print(twolargest())