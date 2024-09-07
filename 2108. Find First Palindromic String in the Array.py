'''
Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

'''
def FirstPalindrome():
    words=["hi","hello","aba","racecar","bye"]
    n=len(words)
    i=0
    while i<n:
        temp=words[i][::-1]
        if temp==words[i]:
            return words[i]
        i+=1
    return ""
print(FirstPalindrome())