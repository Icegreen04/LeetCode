def selectionSort(arr):
    n=len(arr)
    if n<2:
        return arr
    for i in range(n):
        current_min=i
        for j in range(i,n):
           if arr[j]<arr[current_min]:
               current_min=j
        arr[i],arr[current_min]=arr[current_min],arr[i]
    else:
        return arr 

arr=[3,2,10,1,22,1,3,5,8,9]
print(selectionSort(arr))