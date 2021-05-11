import solution
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.processTasks([x[:] for x in test_input])

    def processTasks(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: int
        """
        tasks.append([10**9+1,10**9+1,1])
        # 每个task最晚开启时间为task[i][1] - task[i][2] + 1
        # 最晚启动时间最小的task需要最先被启动
        res, q = 0, []
        for start,end,period in sorted(tasks):
            # 当前的时间需要到start，队列中所有start前需要完成的任务必须完成
            while q and q[0][0] + res < start:
                # 该任务已被完成：当前res大于该任务入队时的res与period的和
                if q[0][0] + res >= q[0][1]:
                    heapq.heappop(q)
                else:
                    # 如果要在start之前结束，那么相当于更新res为该任务入队时的res加上该任务需要的period来完成这个任务
                    # 如果可以在start之后结束，那么相当于更新res为该任务入队时的res加上该任务必须在start之前执行的时间长度
                    res = min(q[0][1], start) - q[0][0]
            # 当前的任务入队，也就意味着队中的任务都已满足开始时间
            heapq.heappush(q, (end+1-period-res,end+1))
        return res
