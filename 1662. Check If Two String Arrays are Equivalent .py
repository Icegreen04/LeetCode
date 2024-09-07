'''
Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.

A string is represented by an array if the array elements concatenated in order forms the string.

Example 1:

Input: word1 = ["ab", "c"], word2 = ["a", "bc"]
Output: true
Explanation:
word1 represents string "ab" + "c" -> "abc"
word2 represents string "a" + "bc" -> "abc"
The strings are the same, so return true.
'''
def EqvStrArr():
    word1=["abc",'vg',"df"]
    word2=["ab","cv","gd","f"]
    return ''.join(word1)==''.join(word2)
print(EqvStrArr())

# SOLUTION 2
def EqvStrArr2():
    word1=["abc",'vg',"df"]
    word2=["ab","cv","gd","f"]
    n1=len(word1)
    n2=len(word2)
    check1=word1[0]
    check2=word2[0]
    i=1
    while i<n1:
        check1=check1+word1[i]
        i+=1
    i=1
    while i<n2:
        check2=check2+word2[i]
        i+=1
    return check1==check2
print(EqvStrArr2())