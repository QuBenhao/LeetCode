import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.defangIPaddr(test_input)

    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        # 20ms solution
        # return address.replace(".","[.]")
        # 4ms solution
        return '[.]'.join(address.split('.'))
