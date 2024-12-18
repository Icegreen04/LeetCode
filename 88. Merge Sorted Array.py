'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

'''
def merge(nums1,nums2,m,n):
    nums1_ptr=m-1
    nums2_ptr=n-1
    end_ptr=m+n-1
    
    while nums1_ptr>=0 and nums2_ptr>=0:
        if nums1[nums1_ptr]>nums2[nums2_ptr]:
            nums1[end_ptr]=nums1[nums1_ptr]
            nums1_ptr-=1
        else:
            nums1[end_ptr]=nums2[nums2_ptr]
            nums2_ptr-=1
        end_ptr-=1
        
    while nums2_ptr>=0:
        nums1[end_ptr]=nums2[nums2_ptr]
        nums2_ptr-=1
        end_ptr-=1
    return nums1
        

nums1=[3,5,6,7,0,0,0,0,0]
nums2=[2,4,5,7,9]
n=len(nums2)
m=0
for i in nums1:
    if i==0:
        break
    else:
        m+=1
print(merge(nums1,nums2,m,n))