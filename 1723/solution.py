import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        jobs, k = test_input
        return self.minimumTimeRequired(list(jobs), k)

    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """

        # answer at least max (k=n) and at most sum (k=1)
        n, left, right = len(jobs), max(jobs), sum(jobs)
        # assign jobs with most time first
        jobs.sort(reverse=True)

        def isPossible(index):
            # assign successfully
            if index == n:
                return True
            for j in range(k):
                if assign[j] >= jobs[index]:
                    # assign jobs[index] to jth person
                    assign[j] -= jobs[index]
                    if isPossible(index+1):
                        return True
                    # backtracking
                    assign[j] += jobs[index]
                # we cannot assign anything to jth person
                if assign[j] == mid:
                    break
            return False

        # binary search
        while left < right:
            mid = (left + right) // 2
            assign = [mid] * k
            # answer is at most mid
            if isPossible(0):
                right = mid
            # cannot assign, answer is at least mid + 1
            else:
                left = mid + 1
        return left
