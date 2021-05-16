import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums1, nums2 = test_input
        return self.nextGreaterElement(nums1.copy(),nums2.copy())

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # for i in range(len(nums1)):
        #     found = False
        #     for j in range(nums2.index(nums1[i]),len(nums2)):
        #         if nums2[j] > nums1[i]:
        #             nums1[i] = nums2[j]
        #             found = True
        #             break
        #     if not found:
        #         nums1[i] = -1
        #
        # return nums1

        answer = {}
        stack = []
        for x in nums2:
            while stack and stack[-1] < x:
                answer[stack[-1]] = x
                del stack[-1]
            stack.append(x)
        for x in stack:
            answer[x] = -1
        return [answer[x] for x in nums1]
