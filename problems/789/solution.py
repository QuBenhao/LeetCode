import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ghosts, target = test_input
        return self.escapeGhosts([x[:] for x in ghosts], list(target))

    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # 启发式: 我们到达终点需要的步数至少是 abs(targetX - 0) + abs(targetY - 0)
        # 敌人可以任意移动，那么存在任意敌人在这或者这之前能到达终点，我们必然就不能走到终点
        # 以上条件可以想象为我们在某些半路会被抓，那么敌人必然可以以同样时间到达终点
        def manhantenDistance(p1, p2):
            return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

        m = manhantenDistance((0, 0), target)
        return all(manhantenDistance(g, target) > m for g in ghosts)
