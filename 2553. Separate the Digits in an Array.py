'''
Given an array of positive integers nums, return an array answer that consists of the digits of each integer in nums after separating them in the same order they appear in nums.

To separate the digits of an integer is to get all the digits it has in the same order.

For example, for the integer 10921, the separation of its digits is [1,0,9,2,1].
 

Example 1:

Input: nums = [13,25,83,77]
Output: [1,3,2,5,8,3,7,7]
Explanation: 
- The separation of 13 is [1,3].
- The separation of 25 is [2,5].
- The separation of 83 is [8,3].
- The separation of 77 is [7,7].
answer = [1,3,2,5,8,3,7,7]. Note that answer contains the separations in the same order.
'''
def SeperateDigits():
    nums=[22,3,11,444,543,6665554433]
    answer=[]
    n=len(nums)
    i=0
    for i in range(n):
        stack=[]
        while nums[i]>0:
            stack.append(nums[i]%10)
            nums[i]=int(nums[i]/10)
        while stack:
            answer.append(stack.pop())
    return answer
print(SeperateDigits())
'''
FAR WORSE SOLUTION PROOVING I NEED TO CHANEG MY APPROACH
        answer=[]
        stack=[]
        n=len(nums)
        i=0
        while i < n:
            if nums[i]==0:
                i+=1
                while stack:
                    answer.append(stack.pop())
                stack=[]
            else:
                stack.append(nums[i]%10)
                nums[i]=int(nums[i]/10)
        return answer
'''
