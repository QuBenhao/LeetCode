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
        from bisect import bisect_left

        def g(a):
            s=set([0])
            for i in a:
                s.update(set([i+j for j in s]))
            return s
        n=len(nums)
        f=g(nums[:n//2])
        s=[-(1<<32)]+sorted(g(nums[n//2:]))+[1<<32]
        z=1<<32
        for i in f:
            z=min(z,abs(i+s[bisect_left(s,goal-i)-1]-goal),abs(i+s[bisect_left(s,goal-i)]-goal))
        return z

        # # function that generates all possible sums of sebsequences
        # def dfs(i, cur, arr, sums):
        #     if i == len(arr):
        #         sums.add(cur)
        #         return
        #     dfs(i + 1, cur, arr, sums)
        #     dfs(i + 1, cur + arr[i], arr, sums)
        #
        # sums1, sums2 = set(), set()
        # # generate all possible sums of the 1st and 2nd half
        # dfs(0, 0, nums[:len(nums) // 2], sums1)
        # dfs(0, 0, nums[len(nums) // 2:], sums2)
        #
        # # sort the possible sums of the 2nd half
        # s2 = sorted(sums2)
        # ans = 10 ** 10
        # # for each possible sum of the 1st half, find the sum in the 2nd half
        # # that gives a value closest to the goal using binary search
        # for s in sums1:
        #     remain = goal - s
        #     i1 = bisect_left(s2, remain)
        #     if i1 < len(s2):
        #         ans = min(ans, abs(remain - s2[i1]))
        #     if i1 > 0:
        #         ans = min(ans, abs(remain - s2[i1 - 1]))
        # return ans
