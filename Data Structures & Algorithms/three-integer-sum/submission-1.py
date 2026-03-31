class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        L = 0
        ans = []
        nums.sort()
        for L in range(n):
            if L > 0 and nums[L] == nums[L-1]:      # to remove duplicate triplets
                continue
            M = L+1
            R = n-1
            while(M<R):
                if((nums[L] + nums[M] + nums[R]) ==0):
                    ans.append([nums[L],nums[M],nums[R]]) 
                    M+=1
                    R-=1

                    while M < R and nums[M] == nums[M-1]:
                        M += 1
                    while M < R and nums[R] == nums[R+1]:
                        R -= 1

                elif((nums[L] + nums[M] + nums[R]) <0):
                    M+=1
                elif((nums[L] + nums[M] + nums[R]) >0):
                    R-=1
        return ans
