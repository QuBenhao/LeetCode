import solution
from math import log


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.pathInZigZagTree(label=test_input)

    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        ans = [label]
        # Initial entry endpoint
        last = 2 ** int(log(label, 2))
        while label > 1:
            # The parent node's distance from its exit endpoint
            add = label - last >> 1
            # Calculate the parent node's value
            label = last - 1 - add
            # The next entry endpoint is half the current one
            last >>= 1
            ans.append(label)
        return ans[::-1]

        # ans = [label]
        # # Initial exit endpoint
        # last = 2 ** (int(log(label, 2)) + 1)
        # while label > 1:
        #     # The parent node's distance from its entry endpoint
        #     dis = last - 1 - label >> 1
        #     # Calculate the parent node's value
        #     label = last // 4 + dis
        #     # The next exit endpoint is obtained by dividing by 2
        #     last >>= 1
        #     ans.append(label)
        # return ans[::-1]
