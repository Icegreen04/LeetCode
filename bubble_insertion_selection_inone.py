def bubbleSort(arr1):
    n=len(arr1)
    if n<2:
        return arr1
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if arr1[j]>arr1[j+1]:
                arr1[j],arr1[j+1]=arr1[j+1],arr1[j]
                swapped=True
        if not swapped:
            return arr1
    else:
        return arr1

def insertionSort(arr1):
    n=len(arr1)
    if n<2:
        return arr1
    for i in range(1,n):
        j=i
        while j>0 and arr1[j-1]>arr1[j]:
            arr1[j-1],arr1[j]=arr1[j],arr1[j-1]
            j-=1
    return arr1

def selectionSort(arr1):
    n=len(arr1)
    if n<2:
        return arr1
    
    for i in range(1,n):
        current_min=i
        for j in range(i,n):
            if arr1[j]<arr1[current_min]:
                j=current_min
        arr1[i],arr1[current_min]=arr1[current_min],arr1[i]
    return arr1
    
def mergeArrs(arr1,arr2,m,n):
    for i in range(n):
        arr1[i+m]=arr2[i]
    if bubbleSort(arr1)==insertionSort(arr1)==insertionSort(arr1):
        return  arr1
    else:
        return "Failed"
 
arr1=[2,2,3,5,0,0,0]
arr2=[1,4,6]
n=len(arr2)
m=0
for i in arr1:
    if i==0:
        break
    else:
        m+=1
print(mergeArrs(arr1,arr2,m,n))