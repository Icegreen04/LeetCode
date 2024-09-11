nums=[2,3,4,5,7,8,10]
target=3
left=0
right=len(nums)-1

while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        flag=1
        break
    elif nums[mid]<target:
        left=mid+1
    else:
        right=mid-1
if flag!=1:
    print(-1)
else:
    print(mid)