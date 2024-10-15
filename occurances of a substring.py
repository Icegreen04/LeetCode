'''
Problem: Find All Occurrences of a Substring
Given a string s and a substring sub, write a function to find all the starting indices of sub in s. You must return the indices in an array in increasing order.
Example 1:

Input: s = "banana", sub = "ana"
Output: [1, 3]
Explanation: The substring "ana" occurs at index 1 and index 3 in the string "banana".
Example 2:

Input: s = "aaaaa", sub = "aa"
Output: [0, 1, 2, 3]
Explanation: The substring "aa" occurs at indices 0, 1, 2, and 3 in the string "aaaaa".
Example 3:

Input: s = "hello", sub = "ll"
Output: [2]
Explanation: The substring "ll" occurs at index 2 in the string "hello".
Example 4:

Input: s = "abc", sub = "d"
Output: []
Explanation: The substring "d" does not occur in the string "abc".

Constraints:
1 <= s.length <= 10^5
1 <= sub.length <= s.length
s and sub consist of only lowercase English letters.
The solution should handle multiple occurrences of the substring efficiently.
'''

#faster method
def findSubString(s,sub):
    indices=[]
    len_s=len(s)
    len_sub=len(sub)
    
    if len_s<len_sub:
        return indices
    
    for i in range(len_s-len_sub+1):
        if s[i:i+len_sub]==sub:
            indices.append(i)
    return indices

s="abaaaahaaaahaa"
sub="haa"
print(findSubString(s,sub))

'''
def findSubString(s,sub):
    indices=[]
    if len(sub)>len(s):
        return indices
    for i in range(len(s)):
        if s[i]!=sub[0]:
            pass
        else:
            for j in range(len(sub)):
                if i+j==len(s):
                    break
                if sub[j]!=s[i+j]:
                    break
            else:
                indices.append(i)

    return indices

s="abaaaaaahaa"
sub="haa"
print(findSubString(s,sub))
'''

