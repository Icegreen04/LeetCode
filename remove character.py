'''
Problem: Remove All Occurrences of a Specified Character
Given a string s and a character char, write a function to remove all occurrences of char from s. Return the modified string.
Example 1:

Input: s = "hello world", char = "l"
Output: "heo word"
Explanation: All occurrences of 'l' are removed from "hello world", resulting in "heo word".
Example 2:

Input: s = "abcdefabc", char = "a"
Output: "bcdefbc"
Explanation: All occurrences of 'a' are removed from "abcdefabc", resulting in "bcdefbc".
Example 3:

Input: s = "aaaaa", char = "a"
Output: ""
Explanation: All occurrences of 'a' are removed from "aaaaa", resulting in an empty string.
Example 4:

Input: s = "leetcode", char = "e"
Output: "ltcod"
Explanation: All occurrences of 'e' are removed from "leetcode", resulting in "ltcod".
Constraints:
0 <= s.length <= 1000
char is a single lowercase English letter.
The string s consists of lowercase English letters.
'''

def removeChar(s,char):
    return s.replace(char,"")

s="hi for this i am harshi"
char="h"
print(removeChar(s,char))
