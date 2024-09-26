'''
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true
'''

from collections import Counter
def isAnagram():
    s="anagram"
    t="naarmag"
    if len(s)!=len(t):
        return False
    else:
        return Counter(s)==Counter(t)
print(isAnagram())
'''
METHOD 2 IS using hashmaps which is implemented below

        smap={}
        for i in s:
            if i in smap:
                smap[i]+=1
            else:
                smap[i]=1
        
        for i in t:
            if i not in smap:
                return False
            else:
                smap[i]-=1
                if smap[i]==0:
                    del smap[i]
        
        # return len(smap)
'''