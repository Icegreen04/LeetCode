'''
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

 

Example 1:

Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 
'''
def KDistinctEle():
    arr=["a","b","d","a","e","c","hh"]
    k=2
    hashset={}
    distinct=[]
    for i in arr:
        if i in hashset:
            hashset[i]+=1
        else:
            hashset[i]=1
            distinct.append(i)
    count=0
    for i in distinct:
        if hashset[i]==1:
            count+=1
            if count==k:
                return i
    return ""
print(KDistinctEle())