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

        jobs.sort(reverse=True)
        n, left, right = len(jobs), jobs[0], sum(jobs)

        def is_possible(index):
            if index == n:
                return True
            for j in range(k):
                # 尝试将第index个任务分配给第j个人
                if assign[j] >= jobs[index]:
                    assign[j] -= jobs[index]
                    # 递归
                    if is_possible(index + 1):
                        return True
                    # 分配给第j个人无法完成其他人的分配
                    assign[j] += jobs[index]
                # 无法分配任何任务给第j个人
                if assign[j] == mid:
                    break
            return False

        while left < right:
            mid = (left + right) // 2
            assign = [mid] * k
            # 分配为最大mid是可行的
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
        #     # 优先分配给没分配过的人
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
