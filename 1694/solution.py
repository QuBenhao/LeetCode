import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reformatNumber(test_input)

    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        n1 = number.replace(" ","")
        n = n1.replace("-","")
        l = len(n)
        if l < 4:
            return n
        result = ""
        index = 0
        while index < l - 4:
            result += n[index:index+3]
            result += "-"
            index += 3
        if l % 3 != 1:
            result += n[index:index+3]
            if index+ 3 < l:
                result += "-"
                result += n[index+3:]
        elif l > 3:
            result += n[index:index+2]
            result += "-"
            result += n[index+2:]
        return result
