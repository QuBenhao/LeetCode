import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numRescueBoats(*test_input)

    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        ans = left = 0
        right = len(people) - 1
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            ans += 1
            right -= 1
        return ans
