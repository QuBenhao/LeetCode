import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subsetsWithDup(list(test_input))

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # import itertools
        # res=[[]]
        # nums.sort()
        # for i in range(1, len(nums)+1):
        #     iter1 = list(set(itertools.combinations(nums, i)))
        #     res += list(iter1)
        # return res

        nums.sort()
        n = len(nums)
        ans = [[]]
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                ans += [x+[(nums[i],i)] for x in ans if x and x[-1][1] == i-1]
            else:
                ans += [x+[(nums[i],i)] for x in ans]
        return [[]] + [list(list(zip(*x))[0]) for x in ans if x]

        # nums.sort()
        # n = len(nums)
        # ans = [[]]
        # for i in range(n):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         ans += [x+[nums[i]] for x in ans[len(ans) - last:]]
        #     else:
        #         last = len(ans)
        #         ans += [x+[nums[i]] for x in ans]
        # return ans
