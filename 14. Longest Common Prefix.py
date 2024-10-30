'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
def LongestCommonPrefix(strs):
    if len(strs)<2:
        return strs[0]
    
    soln=""
    for i in range(len(strs[0])):
        temp=strs[0][i]
        for j in strs:
            try:
                if j[i]!=temp:
                    return soln
            except:
                return soln
        soln+=temp
    return soln

strs=["flower","flow","flight"]
print(LongestCommonPrefix(strs))