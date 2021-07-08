import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.majorityElement(list(test_input))

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 狼人杀归票算法
        # 第一轮找到最可能出局的那个人
        n = len(nums)
        ans = -1
        count = 0
        for num in nums:
            # 没有票数，暂时认为是当前的人
            if not count:
                ans = num
            # 有相同的人上票，票数加一；否则票数减一
            if num == ans:
                count += 1
            else:
                count -= 1
        # 第二轮确定这个人的票数确实过半
        return ans if count and nums.count(ans) > n // 2 else -1

