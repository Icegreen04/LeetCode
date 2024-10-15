'''
check if its a palindrome or not
'''
import re
def isPalindrome(s):
    s=s.strip()
    s= re.sub(r"[^0-9a-zA-Z]",'',s).lower()
    return s==s[::-1]

s="A man, a plan, a canal: Panamaa"
print(isPalindrome(s))