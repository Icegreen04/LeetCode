'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''
def lenLastWord():
    s="  hi i am just a boi"
    s=s.strip()
    count=0
    for i in range(len(s)-1,-1,-1):
        if s[i]!=' ':
            count+=1
        else:
            return count
    return count
print(lenLastWord())