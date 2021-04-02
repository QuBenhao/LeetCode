import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.trap(list(test_input))

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n , lsum, lmax, rsum, rmax = len(height), 0, 0, 0, 0
        for i in range(n):
            lmax = max(lmax, height[i])
            rmax = max(rmax, height[n-1-i])
            lsum += lmax
            rsum += rmax
        return lsum + rsum - max(height) * n - sum(height) if height else 0

        # n, ans = len(height), 0
        # left, right, left_max, right_max = 0, n - 1, 0, 0
        # while left <= right:
        #     if height[left] <= height[right]:
        #         if height[left] > left_max:
        #             left_max = height[left]
        #         else:
        #             # height[left] <= left_max <= height[right]
        #             ans += left_max - height[left]
        #         left += 1
        #     else:
        #         if height[right] > right_max:
        #             right_max = height[right]
        #         else:
        #             ans += right_max - height[right]
        #         right -= 1
        # return ans

        # stack, ans = [], 0
        # for i,v in enumerate(height):
        #     while stack and height[stack[-1]] < v:
        #         # height between left upper and right upper
        #         h = height[stack.pop()]
        #         if not stack:
        #             break
        #         # since the area of lower area has been computed, minus the height
        #         ans += (min(height[stack[-1]], height[i]) - h) * (i - stack[-1] - 1)
        #     stack.append(i)
        # return ans
