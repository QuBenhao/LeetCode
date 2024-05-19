import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, k = test_input
        copy_nums = list(nums)
        self.rotate(copy_nums, k)
        return copy_nums

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Solution 4 Fastest
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1

                if start == current:
                    break
            start += 1

        # Solution 3
        # n = len(nums)
        # k %= n
        # nums[:] = nums[-k:] + nums[:-k]

        # Solution 2 Reverse
        # def reverse(arr, start, end):
        #     while start < end:
        #         arr[start], arr[end] = arr[end], arr[start]
        #         start += 1
        #         end -= 1
        #
        # n = len(nums)
        # k %= n
        # nums.reverse()
        # reverse(nums, 0, k-1)
        # reverse(nums, k, n-1)

        # Solution 1
        # for i in range(k%len(nums)):
        #     nums.insert(0, nums.pop())
