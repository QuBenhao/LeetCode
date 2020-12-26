import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumBinaryString(str(test_input))

    def maximumBinaryString(self, binary):
        """
        :type binary: str
        :rtype: str
        """
        if "0" not in binary or ("10" not in binary and "00" not in binary):
            return binary

        start = binary.index('0')
        start += binary.count('0') - 1
        s = "1" * len(binary)
        return s[:start] + '0' + s[start + 1:]
