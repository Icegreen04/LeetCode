'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
'''
def RansomNote():
    magazine="aabbcfetr"
    ransomNote="abbat"
    magmap={}
    for i in magazine:
        if i in magmap:
            magmap[i]+=1
        else:
            magmap[i]=1
    
    for i in ransomNote:
        if i not in magmap or magmap[i]<=0:
            return False
        else:
            magmap[i]-=1
    else:
        return True
print(RansomNote())
'''
using the counter from collections is arguably faster but i wanted to implement this using hashmaps
from collections import Counter
        magazine_count = Counter(magazine)
        ransomNote_count = Counter(ransomNote)

        for char, count in ransomNote_count.items():
            if magazine_count[char] < count:
                return False
                
        return True
'''