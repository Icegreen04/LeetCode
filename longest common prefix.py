'''
Problem: Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
Example 1:

Input: strs = ["flower", "flow", "flight"]
Output: "fl"
Explanation: The longest common prefix between "flower", "flow", and "flight" is "fl".
Example 2:

Input: strs = ["dog", "racecar", "car"]
Output: ""
Explanation: There is no common prefix between the strings "dog", "racecar", and "car".
Example 3:

Input: strs = ["interspecies", "interstellar", "interstate"]
Output: "inters"
Explanation: The longest common prefix between "interspecies", "interstellar", and "interstate" is "inters".
Example 4:

Input: strs = ["a"]
Output: "a"
Explanation: Since there's only one string, the entire string "a" is the prefix.
Example 5:

Input: strs = ["", "b"]
Output: ""
Explanation: There is no common prefix between an empty string and any other string.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
def longestCommonPrefix(strs):
    if len(strs)==1:
        return strs[0]
    prefix=''
    for i in range(len(strs[0])):
        for j in strs:
           try:
               if j[i]==strs[0][i]:
                   pass
               else:
                   return prefix
           except:
               return prefix
        prefix+=strs[0][i]
    return prefix

strs=["flower", "flow", "flight"]
print(longestCommonPrefix(strs))