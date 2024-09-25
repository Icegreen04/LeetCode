'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

'''
def UniqueNoOccur():
    arr=[2,1,1,3,3,3,4]
    arrMap={}
    freqMap={}
    for i in arr:
        if i in arrMap:
            arrMap[i]+=1
        else:
            arrMap[i]=1
    for i in arrMap.values():
        if i in freqMap:
            return False
        else:
            freqMap[i]=[]
    else:
        return True
print(UniqueNoOccur())