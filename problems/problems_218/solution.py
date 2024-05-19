import solution
from sortedcontainers import SortedDict, SortedList


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getSkyline(list(x[:] for x in test_input))

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # ans = []
        # changes = []
        # for left, right, height in buildings:
        #     changes.append((left, -height))
        #     changes.append((right, height))
        # changes.sort()
        # lives = SortedDict()
        # lives[0] = 1
        # for x, h in changes:
        #     # 加入建筑
        #     if h < 0:
        #         if h in lives:
        #             lives[h] += 1
        #         else:
        #             lives[h] = 1
        #             # 最高建筑
        #             if h == lives.keys()[0]:
        #                 ans.append([x, -h])
        #     # 删除建筑
        #     else:
        #         lives[-h] -= 1
        #         if not lives[-h]:
        #             lives.pop(-h)
        #             # 判断最高建筑是否发生变化了
        #             new_max = lives.keys()[0]
        #             if -new_max < h:
        #                 ans.append([x, -new_max])
        # return ans

        ans = []
        changes = []
        for left, right, height in buildings:
            changes.append((left, -height))
            changes.append((right, height))
        # 按变化点的先后排序
        changes.sort()
        # 同样默认有个高度为0
        lives = SortedList([0])
        # 上一个建筑最高高度
        prev = 0
        for x, h in changes:
            # 根据h大小加入或删除建筑
            if h < 0:
                lives.add(h)
            else:
                lives.remove(-h)
            # 加入或删除后当前的最高高度
            curr_max = -lives[0]
            # 最高高度发生了变化
            if curr_max != prev:
                ans.append([x, curr_max])
            prev = curr_max
        return ans
