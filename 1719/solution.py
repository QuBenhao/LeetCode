import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkWays([x[:] for x in test_input])

    def checkWays(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        import collections, copy
        state = []
        self.ans = 0
        actions = collections.defaultdict(list)
        for i in range(len(pairs)):
            if pairs[i][0] not in state:
                state.append(pairs[i][0])
            if pairs[i][1] not in state:
                state.append(pairs[i][1])
            actions[pairs[i][0]].append(pairs[i][1])
            actions[pairs[i][1]].append(pairs[i][0])

        def construct(state, actions):
            print(state, actions)
            if not state:
                self.ans += 1
                return
            for root in state:
                if len(actions[root]) == len(state) - 1:
                    temp = list(state)
                    temp_ = copy.deepcopy(actions)
                    for n in temp_[root]:
                        temp_[n].remove(root)
                        if len(temp_[n]) == 0:
                            temp.remove(n)
                    temp.remove(root)
                    temp_.pop(root)
                    construct(temp, temp_)
            return

        construct(state, actions)
        return self.ans
