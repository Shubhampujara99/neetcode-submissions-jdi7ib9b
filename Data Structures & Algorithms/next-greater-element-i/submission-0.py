class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        n2 = len(nums2)
        L = 0
        ans = []
        while(L<n1):
            found = False
            idx = nums2.index(nums1[L]) 
            for R in range(idx+1, n2):
                if(nums1[L]<nums2[R]):
                    found = True
                    ans.append(nums2[R])
                    break
            if(found==False):
                ans.append(-1)
            L+=1
        return ans

