def insertionSort(arr):
    n=len(arr)
    if n<2:
        return arr
    
    for i in range(1,n):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    else:
        return arr
        
arr=[3,2,1,5,6,10,3,2,4,46,0]
print(insertionSort(arr))
