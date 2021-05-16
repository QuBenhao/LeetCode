import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, goal = test_input
        return self.minAbsDifference(list(nums), goal)

    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        n = len(nums)
        nums.sort(key=lambda x: -abs(x))
        neg = [0 for _ in range(n + 1)]
        pos = [0 for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            if nums[i] < 0:
                neg[i] = neg[i + 1] + nums[i]
                pos[i] = pos[i + 1]
            else:
                pos[i] = pos[i + 1] + nums[i]
                neg[i] = neg[i + 1]
        ans = abs(goal)
        s = set([0])

        def check(a, b):
            if b < goal - ans or goal + ans < a:
                return False
            return True

        for i in range(n):
            sl = [x for x in s if check(x + neg[i], x + pos[i])]
            if len(sl) == 0:
                break
            s = set(sl)
            for x in sl:
                y = x + nums[i]
                if abs(y - goal) < ans:
                    ans = abs(y - goal)
                if ans == 0:
                    return 0
                s.add(y)
        return ans
