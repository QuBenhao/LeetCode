import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countBits(test_input)

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        curr = 0
        ans = [0]
        while curr < num:
            new = []
            for i in ans:
                if curr == num:
                    return ans + new
                new.append(1+i)
                curr += 1
            ans += new
        return ans

        # Solution 2:
        # bits = [0]
        # highBit = 0
        # for i in range(1, num + 1):
        #     if i & (i - 1) == 0:
        #         highBit = i
        #     bits.append(bits[i - highBit] + 1)
        # return bits

        # Solution 3:
        # bits = [0]
        # for i in range(1, num + 1):
        #     bits.append(bits[i >> 1] + (i & 1))
        # return bits

        # Solution 4:
        # bits = [0]
        # for i in range(1, num + 1):
        #     bits.append(bits[i & (i - 1)] + 1)
        # return bits
