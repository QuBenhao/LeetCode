import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nextGreaterElement(test_input)

    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n >= 2147483647:
            return -1

        nums = [int(i) for i in str(n)]

        index = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                index = i
                break

        if index == -1:
            return -1

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[index]:
                temp = nums[i]
                nums[i] = nums[index]
                nums[index] = temp
                break

        nums = nums[:index+1] + sorted(nums[index+1:])

        strings = [str(i) for i in nums]
        num = "".join(strings)
        num = int(num)

        if num > 2147483647:
            return -1
        return num
