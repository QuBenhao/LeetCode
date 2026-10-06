import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.escapeGhosts(*test_input)

    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        # Heuristic: reaching the target takes at least abs(targetX - 0) + abs(targetY - 0) steps
        # Enemies can move freely; if any enemy can reach the target by then, we cannot reach it safely
        # To see why, if an enemy can catch us along the way, it can also follow our remaining path and reach the target at the same time
        def manhantenDistance(p1, p2):
            return abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])

        m = manhantenDistance((0, 0), target)
        return all(manhantenDistance(g, target) > m for g in ghosts)
