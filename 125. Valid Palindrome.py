'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
'''
import re

def cleanText(text):
    text=re.sub(r'[^a-zA-Z0-9]','',text)
    text=text.lower()
    return text

def isPalindrome(text):
    text=cleanText(text)
    left=0
    right=len(text)-1
    while left<=right:
        if text[left]!=text[right]:
            return False
        else:
            left+=1
            right-=1
    else:
        return True

print(isPalindrome("A man, a plan, a canal: Panama  ::;"))