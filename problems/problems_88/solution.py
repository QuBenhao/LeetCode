import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums1, m, nums2, n = test_input
        nums1 = nums1.copy()
        self.merge(nums1, m, list(nums2), n)
        return nums1

    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m > 0 and n > 0 and nums1[m-1] >= nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            self.merge(nums1,m-1,nums2,n)
        elif n > 0:
            nums1[m+n-1] = nums2[n-1]
            self.merge(nums1,m,nums2,n-1)

        # if m == 0:
        #     for i in range(n):
        #         nums1[i] = nums2[i]
        # else:
        #     insert_index = m + n - 1
        #     n1_index = m-1
        #     n2_index = n-1
        #     while n2_index >= 0:
        #         if n1_index >= 0 and nums1[n1_index] >= nums2[n2_index]:
        #             nums1[insert_index] = nums1[n1_index]
        #             n1_index -= 1
        #             insert_index -= 1
        #         else:
        #             nums1[insert_index] = nums2[n2_index]
        #             n2_index -= 1
        #             insert_index -= 1
