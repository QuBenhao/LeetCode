import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        fronts, backs = test_input
        return self.flipgame(fronts,backs)

    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        not_good = set()
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                not_good.add(fronts[i])
        x = fronts + backs
        list.sort(x)
        for i in x:
            if i not in not_good:
                return i
        return 0
