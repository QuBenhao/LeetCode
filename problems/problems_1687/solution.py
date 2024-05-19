import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.boxDelivering(*test_input)

    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """

        # dp[i]: min trips for delivering ith boxes
        dp = [0] * (len(boxes) + 1)

        index = ports_count = num_box = weight = 0

        # load ith box
        for i in range(len(boxes)):
            num_box += 1
            weight += boxes[i][1]

            # count for ports that needs a trip
            if i == 0 or boxes[i][0] != boxes[i-1][0]:
                ports_count += 1

            # we cannot carry more than maxBoxes, maxWeight boxes
            # if we could load index+1 boxes as the same trip as index boxes, we should always load more
            while num_box > maxBoxes or weight > maxWeight or (index < i and dp[index] == dp[index+1]):
                num_box -= 1
                weight -= boxes[index][1]
                if boxes[index][0] != boxes[index+1][0]:
                    ports_count -= 1
                # index ++ also means we cannot load boxes from current index to i
                index += 1

            # dp[index] is the best solution to load index boxes,
            # ports_count is the min trips needed for load boxes from index+1 to i+1,
            # plus 1 for return storage
            dp[i+1] = dp[index] + ports_count + 1

        return dp[len(boxes)]
