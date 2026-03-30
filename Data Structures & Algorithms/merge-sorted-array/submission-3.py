class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        L = 0
        R = 0
        nums1[:] = nums1[:m]
        while R < n:            
            if L >= len(nums1):
                nums1.append(nums2[R])
                R += 1            
            elif nums2[R] <= nums1[L]:
                nums1.insert(L, nums2[R])
                R += 1
            else:
                L += 1
