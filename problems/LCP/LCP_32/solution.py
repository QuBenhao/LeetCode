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
        # The latest start time of each task is task[i][1] - task[i][2] + 1
        # The task with the earliest latest-start time must start first
        res, q = 0, []
        for start,end,period in sorted(tasks):
            # Advance the current time to start; all queued tasks due before start must be completed
            while q and q[0][0] + res < start:
                # This task is complete: the current res exceeds res at enqueue time plus period
                if q[0][0] + res >= q[0][1]:
                    heapq.heappop(q)
                else:
                    # If the task must finish before start, complete it by setting res to res at enqueue time plus its required period
                    # If it may finish after start, set res to res at enqueue time plus the time it must run before start
                    res = min(q[0][1], start) - q[0][0]
            # Enqueue the current task; all queued tasks have now reached their start times
            heapq.heappush(q, (end+1-period-res,end+1))
        return res
