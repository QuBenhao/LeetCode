import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.plusOne(test_input)

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i] += carry
            if digits[i] > 9:
                carry = 1
                digits[i] = 0
                if i == 0:
                    list.insert(digits,0,carry)
                    return digits
            else:
                carry = 0
                return digits
        return digits

