import solution
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestChair(*test_input)

    def smallestChair(self, times, targetFriend):
        """
        :type times: List[List[int]]
        :type targetFriend: int
        :rtype: int
        """
        n = len(times)
        times = sorted(enumerate(times), key=lambda x:(x[1][0],x[0],-x[1][1]))
        curr = []
        avl = [i for i in range(n)]
        for i, (arr, leave) in times:
            while curr and curr[0][0] <= arr:
                _,idx = heapq.heappop(curr)
                heapq.heappush(avl, idx)
            c = heapq.heappop(avl)
            if i == targetFriend:
                return c
            heapq.heappush(curr, (leave, c))
        return -1
