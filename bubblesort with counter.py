def counter(count):
    count=+1
    return count  

def bubbleSort(arr):
    n=len(arr)
    if n<2:
        return arr
    count=0
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
                count+=counter(count)
        if not swapped:
            break
        print(arr)
    return arr, count
    
arr=[9,4,2,10,4,5]
print(bubbleSort(arr))