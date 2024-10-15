'''
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and the initial word order.
Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "Hello World"
Output: "olleH dlroW"
Example 3:

Input: s = "Python is fun"
Output: "nohtyP si nuf"

Constraints:
1 <= s.length <= 5 * 10^4
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
'''
#faster much better way
def individualReverse(word):
    return word[::-1]

def wordReverse(s):
    s=s.strip()
    words=s.split(' ')
    reversed_words=[]
    for word in words:
        reversed_words.append(individualReverse(word))
    return ' '.join(reversed_words) 

s=" hello this is it"
print(wordReverse(s))
'''
def individualReverse(word):
    return word[::-1]

def wordReverse(s):
    s=s.strip()
    n=len(s)
    NewS=""
    left=0
    right=0
    while right<n:
        if s[right]!= " ":
            right+=1
        else:
            NewS+=individualReverse(s[left:right])
            NewS+=" "
            right+=1
            left=right
    NewS+=individualReverse(s[left:right])
    return NewS

s=" Hello this is It"
print(wordReverse(s))

'''
