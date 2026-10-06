import solution
from collections import defaultdict, deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.circularArrayLoop(list(test_input))

    mark = 1001
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            # Already checked
            if nums[i] >= self.mark:
                continue
            # Starting point i, marker value, and previous value
            cur, tag, last = i, self.mark + i, -1
            # Whether the cycle must contain all positive or all negative values
            flag = nums[cur] > 0
            while True:
                # Next node
                nxt = (cur + nums[cur]) % n
                # Current value
                last = nums[cur]
                # Mark the array entry as visited
                nums[cur] = tag
                # Move to the next node
                cur = nxt
                # Back at the starting point; stop
                if cur == i:
                    break
                # Back at a marked node; stop
                if nums[cur] >= self.mark:
                    break
                # The next two cases involve opposite signs and violate the requirements, so stop
                if flag and nums[cur] < 0:
                    break
                if not flag and nums[cur] > 0:
                    break
            # A valid cycle requires that the final node does not point to itself and its current value equals this traversal's marker
            if last % n != 0 and nums[cur] == tag:
                return True
        return False

        # n = len(nums)
        # connect = defaultdict(list)
        # marks = deque([])
        # for i, num in enumerate(nums):
        #     nxt = (i + num) % n
        #     connect[nxt].append(i)
        #     if nxt == i or nums[nxt] * num < 0:
        #         marks.append(i)
        #         nums[i] = 0
        # while marks:
        #     i = marks.popleft()
        #     for nxt in connect[i]:
        #         if nums[nxt]:
        #             nums[nxt] = 0
        #             marks.append(nxt)
        # return any(num for num in nums)
