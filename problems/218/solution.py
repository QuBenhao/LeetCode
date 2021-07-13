import solution
from sortedcontainers import SortedDict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getSkyline(list(x[:] for x in test_input))

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        changes = []
        for left, right, height in buildings:
            changes.append((left, -height))
            changes.append((right, height))
        changes.sort()
        lives = SortedDict()
        lives[0] = 1
        for x, h in changes:
            # 加入建筑
            if h < 0:
                if h in lives:
                    lives[h] += 1
                else:
                    lives[h] = 1
                    # 最高建筑
                    if h == lives.keys()[0]:
                        ans.append([x, -h])
            # 删除建筑
            else:
                lives[-h] -= 1
                if not lives[-h]:
                    lives.pop(-h)
                    # 判断最高建筑是否发生变化了
                    new_max = lives.keys()[0]
                    if -new_max < h:
                        ans.append([x, -new_max])
        return ans
