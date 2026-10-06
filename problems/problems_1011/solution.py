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
        # Can max_weight carry all the goods within D days?
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

        # The lower bound must cover both the heaviest item and the average daily load; the upper bound is the total weight, shipped in one day
        left, right = max(sum(weights) // D, max(weights)), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if helper(mid):
                left = mid + 1
            else:
                right = mid
        return left
