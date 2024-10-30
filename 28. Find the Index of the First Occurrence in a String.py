'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
'''
def strStr(haystack,needle):
    n_needle=len(needle)
    n=len(haystack)
    if n<n_needle:
        return -1
    if needle==haystack:
        return 0
    for i in range(0,n-n_needle+1):
        if haystack[i:i+n_needle]==needle:
            return i
    else:   
        return -1
haystack="leetcode"
needle="leeto"
print(strStr(haystack,needle))