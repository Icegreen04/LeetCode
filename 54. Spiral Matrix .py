'''
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
'''
def spiralOrder(arr):
    m,n=len(arr),len(arr[0])
    row_start=0
    row_end=m-1
    column_start=0
    column_end=n-1
    
    spiral_arr=[]
    while row_start<=row_end and column_start<=column_end:
        for i in range(column_start,column_end+1):
            spiral_arr.append(arr[row_start][i])
        row_start+=1
        print("segment1")
        
        if row_end<row_start:
            break
        for i in range(row_start,row_end+1):
            spiral_arr.append(arr[i][column_end])
        column_end-=1
        print("segment2")
        
        if column_end<column_start:
            break
        for i in range(column_end,column_start-1,-1):
            spiral_arr.append(arr[row_end][i])
        row_end-=1
        print("segment3")
        for i in range(row_end,row_start-1,-1):
            spiral_arr.append(arr[i][column_start])
        column_start+=1
        print("segment4")
    return spiral_arr
#'''
arr=[[1,2,3,4,5],
     [6,7,8,9,10],
     [11,12,13,14,15],
     [16,17,18,19,20],
     [21,22,23,24,25]]
 #    '''
'''
arr=[[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12]]
     '''
print(spiralOrder(arr))