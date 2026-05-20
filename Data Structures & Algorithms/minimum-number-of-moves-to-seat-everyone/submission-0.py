class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        n = len(seats)
        ans = 0
        for i in range(n):
            ans += abs(seats[i]-students[i])
        return ans