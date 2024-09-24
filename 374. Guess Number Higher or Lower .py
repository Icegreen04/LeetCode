
'''
        We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
This code wont work without the guess api so i have made some slight changes
'''
import random
global num 
n=1000000000
num=random.randint(1,n)
print(num)

def NumChecker(guess):
    if guess==num:
        return 0
    elif guess<num:
        return 1
    else:
        return -1

def GuessNumHighLow():
    left=1
    right=n
    while left<=right:
        mid=(left+right)//2
        result=NumChecker(mid)
        
        if result==0:
            return mid
        elif result==1:
            left=mid+1
        else:
            right=mid-1

print(GuessNumHighLow())