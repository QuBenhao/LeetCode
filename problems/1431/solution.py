import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kidsWithCandies(*test_input)

    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_num = max(candies)
        bool_list = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_num:
                bool_list.append(True)
            else:
                bool_list.append(False)
        return bool_list
