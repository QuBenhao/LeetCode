import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shipWithinDays(*test_input)

    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        # max_weight能否在D天内运载全部货物
        def helper(max_weight):
            count = count_w = 0
            for w in weights:
                count_w += w
                if count_w > max_weight:
                    count += 1
                    count_w = w
            if count_w:
                count += 1
            return count > D

        # 左边界至少要比最大的货物重，也要比每天平均货物大；右边界至多是全部的和，一天运完
        left, right = max(sum(weights) // D, max(weights)), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                left = mid + 1
            else:
                right = mid
        return left
