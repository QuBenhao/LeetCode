import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        weights, D = test_input
        return self.shipWithinDays(list(weights), D)

    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """

        def helper(max_weight):
            count = count_w = 0
            for w in weights:
                count_w += w
                if count_w > max_weight:
                    count += 1
                    count_w = w
                elif count_w == max_weight:
                    count += 1
                    count_w = 0
            if count_w:
                count += 1
            return count > D

        left, right = max(sum(weights) // D, max(weights)), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                left = mid + 1
            else:
                right = mid
        return left
