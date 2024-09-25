'''
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

 

Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
'''
def LetterGrtrTarget():
    letters=["a","c","f","t","x"]
    target="c"
    left=0
    right=len(letters)-1
    if target>=letters[-1]:
        return letters[0]
    while left<=right:
        mid=(left+right)//2
        if letters[mid]>target:
            right=mid-1
        else:
            left=mid+1
    return letters[left]
print(LetterGrtrTarget())
