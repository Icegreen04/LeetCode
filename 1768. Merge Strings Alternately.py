'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
'''
def MergeStrAlt():
    word1="abcdtetgegge"
    word2="harssss"
    l1=len(word1)
    l2=len(word2)
    word=""
    if l1==l2:
        for i in range(len(word1)):
            word+=word1[i]
            word+=word2[i]
    elif l1<l2:
        for i in range(len(word1)):
            word+=word1[i]
            word+=word2[i]
        word+=word2[l1:]
    else:
        for i in range(len(word2)):    
            word+=word1[i]
            word+=word2[i]
        word+=word1[l2:]
    return word
print(MergeStrAlt())
"""
arguably the faster method is using arrays as strings in python are immutable so each time
we do word+=  what we see is that python creates a new string

l1=len(word1)
        l2=len(word2)
        result=[]
        for i in range(min(l1,l2)):
            result.append(word1[i])
            result.append(word2[i])

        if l1<l2:
            result.append(word2[l1:])
        elif l2<l1:
            result.append(word1[l2:])
        return ''.join(result) 
    """