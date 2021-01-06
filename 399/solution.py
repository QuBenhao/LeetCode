import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        equations, values, queries = test_input
        return self.calcEquation([x[:] for x in equations], list(values), [x[:] for x in queries])

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        actions = dict()
        for i in range(len(equations)):
            equation, value = equations[i], values[i]
            a, b = equation
            if a in actions.keys():
                actions[a].append([b, value])
            else:
                actions[a] = [[b, value]]
            if b in actions.keys():
                actions[b].append([a, 1.0 / value])
            else:
                actions[b] = [[a, 1.0 / value]]

        def dfs(init_state, goal_state):
            if init_state not in actions.keys() or goal_state not in actions.keys():
                return -1.0
            frontier = [[init_state,1.0]]
            explored = []
            while frontier:
                state,val = frontier.pop()
                if state == goal_state:
                    return val
                explored.append(state)
                for successor in actions[state]:
                    if successor[0] in explored:
                        continue
                    else:
                        frontier.append([successor[0],successor[1] * val])
            return -1.0

        ans = []
        for query in queries:
            init_state, goal_state = query
            ans.append(dfs(init_state, goal_state))
        return ans
