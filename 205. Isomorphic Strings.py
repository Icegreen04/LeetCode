'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.

'''
def IsomorphicCheck():
    s="badc"
    t="baba"
    forwardMap={}
    reverseMap={}
    for i,j in zip(s,t):
        if i not in forwardMap:
            forwardMap[i]=j
        else:
            if forwardMap[i] !=j:
                return False
        if j not in reverseMap:
            reverseMap[j]=i
        else:
            if reverseMap[j]!=i:
                return False
    else:
        return True
    
print(IsomorphicCheck())