class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        n = int(len(arr) / 2)
        print(n)
        if len(arr) % 2 != 0:
            return arr[n]
        else:
            return (arr[n-1] + arr[n])/2
            
