import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.fractionAddition(test_input)

    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """

        def str_to_float(numstr):
            fraction = numstr.split("/")
            numerator = int(fraction[0])
            denominator = int(fraction[1])
            return numerator, denominator

        def greatest_common_divisor(m, n):
            while n != 0:
                temp = m % n
                m = n
                n = temp
            return m

        def least_common_multiple(m, n):
            return int(m * n / greatest_common_divisor(m, n))

        nums = []
        opearator = []
        num = ""
        start = 0
        if expression[0] == "-":
            num += "-"
            start = 1
        for i in range(start, len(expression)):
            if expression[i] == "+" or expression[i] == "-":
                nums.append(str_to_float(num))
                opearator.append(expression[i])
                num = ""
            else:
                num += expression[i]
        nums.append(str_to_float(num))
        n_start, d_start = nums.pop(0)
        for num in nums:
            n_curr, d_curr = num
            if d_start != d_curr:
                lcm = least_common_multiple(d_start, d_curr)
                n_start *= lcm / d_start
                n_curr *= lcm / d_curr
                d_start = lcm
            if opearator.pop(0) == "+":
                n_start += n_curr
            else:
                n_start -= n_curr
        if n_start == 0:
            d_start = 1
        elif greatest_common_divisor(n_start,d_start) != 1:
            gcd = greatest_common_divisor(n_start,d_start)
            n_start /= gcd
            d_start /= gcd
        return str.format("{}/{}", int(n_start), int(d_start))
