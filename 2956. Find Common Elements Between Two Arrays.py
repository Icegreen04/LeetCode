'''
You are given two integer arrays nums1 and nums2 of sizes n and m, respectively. Calculate the following values:

answer1 : the number of indices i such that nums1[i] exists in nums2.
answer2 : the number of indices i such that nums2[i] exists in nums1.
Return [answer1,answer2].

Example 1:

Input: nums1 = [2,3,2], nums2 = [1,2]

Output: [2,1]
'''

def CommonEle():
    nums1=[2,2,5,6,7,8,4,3]
    nums2=[0,0,2]
    hash1={}
    for ele in nums1:
        if ele in hash1:
            hash1[ele]+=1
        else:
            hash1[ele]=1
    hash2={}
    for ele in nums2:
        if ele in hash2:
            hash2[ele]+=1
        else:
            hash2[ele]=1
    common = set(hash1.keys())&set(hash2.keys())
    n1=0
    n2=0
    for i in common:
        v1=hash1[i]
        n1+=v1
        v2=hash2[i]
        n2+=v2
    return [n1,n2]
print(CommonEle())
'''
not sure if this is better or worse but the code is smaller
hash1 = Counter(nums1)
        hash2 = Counter(nums2)

        common = set(hash1.keys()) & set(hash2.keys())

        n1 = sum(hash1[key] for key in common)
        n2 = sum(hash2[key] for key in common)

        return [n1, n2]
'''