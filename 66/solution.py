import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.plusOne(test_input)

    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1,-1,-1):
            digits[i] += 1
            if digits[i] > 9:
                digits[i] = 0
                if i == 0:
                    list.insert(digits,0,1)
                    return digits
            else:
                return digits
