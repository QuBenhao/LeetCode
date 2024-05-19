import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.beautySum(str(test_input))

    def beautySum(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        # store all freq tables for each iterate
        li = []
        for c in s:
            # we will have a new freq table start from this char
            new = [0] * 26
            i = ord(c) - ord('a')
            new[i] = 1
            # for every freq tables from last iterate
            for counter in li:
                # add curr char to the table first
                counter[i] += 1
                # calculate diff between max and min
                ans += max(counter) - min(k for k in counter if k)
            # add the new freq table for next iterate
            li.append(new)
        return ans
