'''
Given two arrays of integers nums and index. Your task is to create target array under the following rules:

Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.

It is guaranteed that the insertion operations will be valid.

Example 1:

Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

'''
def TargetArrayOrder():
    nums=[3,5,2,1,1,5]
    index=[2,2,0,1,3,3]
    arr=[]
    for i in range(len(nums)):
        arr.insert(index[i],nums[i])
    return arr
print(TargetArrayOrder())
'''
this uses an inbuilt function else we can use a manual shift too:

n=len(nums)
        arr=[None]*n
        for i in range(len(nums)):
            if arr[index[i]]==None:
                arr[index[i]]=nums[i]
            else:
                insert=index[i]
                j=n-1
                while j>=insert:
                    arr[j]=arr[j-1]
                    j-=1
                arr[insert]=nums[i]
        return arr

'''