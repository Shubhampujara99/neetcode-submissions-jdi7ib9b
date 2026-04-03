class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        n = len(people)
        ans = 0

        for i in range(n-1,0,-1):
            if(people[i]==limit):
                ans+=1
                people.pop(i)

        l = 0
        n = len(people)
        r = n-1
        count = 0
        while l <= r:
            wt = people[l] + people[r]
            if wt <= limit:
                l += 1
            r -= 1
            ans += 1

        return ans
        
            
            