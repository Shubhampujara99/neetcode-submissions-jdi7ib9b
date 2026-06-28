class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = 0
        for i in range(k+1):
            ans = max(sum(cardPoints[:i])+ sum(cardPoints[-(k-i):]  if k-i > 0 else []),ans)
        return ans