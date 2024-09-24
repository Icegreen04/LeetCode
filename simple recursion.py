import sys
sys.setrecursionlimit(10000)
def sum(num):
    if num==1:
        return 1
    return num + sum(num-1)

if __name__=='__main__':
    print(sum(9000))