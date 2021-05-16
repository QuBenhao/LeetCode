import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minJumps(test_input.copy())

    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        # n = len(arr)
        # if n <= 1:
        #     return 0
        #
        # graph = {}
        # for i in range(n):
        #     if arr[i] in graph:
        #         graph[arr[i]].append(i)
        #     else:
        #         graph[arr[i]] = [i]
        #
        # curs = [0]  # store current layers
        # visited = {0}
        # step = 0
        #
        # # when current layer exists
        # while curs:
        #     nex = []
        #
        #     # iterate the layer
        #     for node in curs:
        #         # check if reached end
        #         if node == n-1:
        #             return step
        #
        #         # check same value
        #         for child in graph[arr[node]]:
        #             if child not in visited:
        #                 visited.add(child)
        #                 nex.append(child)
        #
        #         # clear the list to prevent redundant search
        #         graph[arr[node]] = []
        #
        #         # check neighbors
        #         for child in [node-1, node+1]:
        #             if 0 <= child < len(arr) and child not in visited:
        #                 visited.add(child)
        #                 nex.append(child)
        #
        #     curs = nex
        #     step += 1

        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  # store layers from start
        visited = {0, n-1}
        step = 0

        other = [n-1] # store layers from end

        # when current layer exists
        while curs:
            # search from the side with fewer nodes
            if len(curs) > len(other):
                curs, other = other, curs
            nex = []

            # iterate the layer
            for node in curs:

                # check same value
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1