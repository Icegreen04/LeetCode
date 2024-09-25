'''
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
'''
def GroupAnagram():    
    anagram={}
    strs=["eat","tea","tan","ate","nat","bat"]
    for s in strs:
        temp=tuple(sorted(s))
        if temp in anagram:
            anagram[temp].append(s)
        else:
            anagram[temp]=[s]
    return anagram.values()
print(GroupAnagram())