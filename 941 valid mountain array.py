'''
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
'''
def MountainArray():
    arr=[2,4,5,7,8,6,4,3,3,2]
    n=len(arr)
    if n<3:
        return False

    i=0
    while i+1<n and arr[i]<arr[i+1]:
        i+=1

    if i==0 or i==n-1:
        return False

    while i+1<n and arr[i]>arr[i+1]:
        i+=1

    if i==n-1:
        return True
    else:
        return False

print(MountainArray())