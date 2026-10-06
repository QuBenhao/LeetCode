import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumTimeRequired(*test_input)

    def minimumTimeRequired(self, jobs, k):
        """
        :type jobs: List[int]
        :type k: int
        :rtype: int
        """

        jobs.sort(reverse=True)
        n, left, right = len(jobs), jobs[0], sum(jobs)

        def is_possible(index):
            if index == n:
                return True
            for j in range(k):
                # Try assigning task index to worker j
                if assign[j] >= jobs[index]:
                    assign[j] -= jobs[index]
                    # Recursion
                    if is_possible(index + 1):
                        return True
                    # Assigning it to worker j leaves no valid assignment for the remaining tasks
                    assign[j] += jobs[index]
                # No task can be assigned to worker j
                if assign[j] == mid:
                    break
            return False

        while left < right:
            mid = (left + right) // 2
            assign = [mid] * k
            # An assignment with maximum load mid is feasible
            if is_possible(0):
                right = mid
            else:
                left = mid + 1
        return right

        # assign, n = [0] * k, len(jobs)
        #
        # def dfs(index, nxt, curr_max, ans):
        #     if curr_max >= ans:
        #         return float("inf")
        #     if index == n:
        #         return curr_max
        #     # Prioritize workers who have not received a task
        #     if nxt < k:
        #         assign[nxt] = jobs[index]
        #         ans = min(ans, dfs(index + 1, nxt + 1, max(curr_max, assign[nxt]), ans))
        #         assign[nxt] = 0
        #     for i in range(nxt):
        #         assign[i] += jobs[index]
        #         ans = min(ans, dfs(index+1, nxt, max(curr_max, assign[i]), ans))
        #         assign[i] -= jobs[index]
        #     return ans
        #
        # return dfs(0, 0, 0, float("inf"))
