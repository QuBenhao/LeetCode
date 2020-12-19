import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxWidthRamp(test_input.copy())

    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Extending on below idea, we first create a decreasing stack (anything higher in between the elements in
        # stack, we have a better replacement or something smaller to the left of it). Then we traverse the array
        # reversely. For every j, we keep popping stack[-1] until we find the element furthest to the left. The
        # reason we can pop is because next j (j-1) to that element to be popped won't be better than this current j
        # (which is farther from the element to be popped).We then continue on with j to find the next j that's
        # greater than stack[-1], where we stopped previously

        stack = []
        n = len(A)
        res = 0
        for i in range(n):
            if not stack or A[stack[-1]] > A[i]:
                stack.append(i)
        for j in range(n)[::-1]:
            while stack and A[j] >= A[stack[-1]]:
                print(j,stack)
                res = max(res, j - stack.pop())
        return res
        # the idea is to keep a decreasing stack. When you encounter something bigger than stack[-1], binary search
        # the left most element in stack that's smaller than it and calculate the distance. Key here is we don't need
        # to put this element in stack since we already have something smaller in stack that will perform better (
        # longer distance) than this current element when we later on encounter something bigger than this current
        # element.
        # stack = []
        # res = 0
        # for j in range(len(A)):
        #     if not stack or A[stack[-1]] > A[j]:
        #         stack.append(j)
        #     else:
        #         index = self.binarySearch(A, stack, A[j])
        #         if index < len(stack):
        #             res = max(res, j-stack[index])
        # return res
        #
        # def binarySearch(A, s, num):
        #     left, right = 0, len(s)
        #     while left < right:
        #         mid = (left+right) // 2
        #         if A[s[mid]] <= num:
        #             right = mid
        #         else:
        #             left = mid+1
        #     return left
