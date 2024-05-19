import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumDeviation(list(test_input))

    def minimumDeviation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        if start is even even: you get all by simlply dividing until odd
        if start is odd you get all, by simply muliplying once

        todo:
         - make all odd numbers even
         - Create 30 deques
         - divide always greatest number
         - update ret min(greates, min)
         - after a number get divided put in lower deque
         - always choose the greatest number from all deques
        runtime 10**5 numbers * 30 * log(30)
        """

        import heapq
        from collections import deque
        for i in range(len(nums)):
            if nums[i] & 1:
                nums[i] <<= 1

        ret = float('inf')
        alr = set()
        nums.sort()
        minE = nums[0]
        n = len(nums)
        nums = deque(nums)
        l = [nums] + [deque() for _ in range(29)]
        heap = [(-nums[-1], 0)]
        # print(l)
        while heap:
            number, index = heapq.heappop(heap)
            l[index].pop()
            number = - number
            if number in alr:
                if l[index]:
                    heapq.heappush(heap, (-l[index][-1], index))
            else:
                alr.add(number)
                ret = min(ret, number - minE)
                if int(number) & 1:
                    break

                new_number = number / 2
                minE = min(minE, new_number)

                # if we encounter the first odd element, its game over (can't make it any smaller)

                # add element to new deque and maybe add it to heap as well
                l[index + 1].appendleft(new_number)
                if len(l[index + 1]) == 1:
                    heapq.heappush(heap, (-new_number, index + 1))

                # add next element from current deque to heap
                if l[index]:
                    heapq.heappush(heap, (-l[index][-1], index))
        return ret

        # import heapq
        # l = []
        # max_min = 0
        # for num in nums:
        #     temp = num
        #     while temp % 2 == 0:
        #         temp //= 2
        #     max_min = max(max_min, temp)
        #     # store the range of each num
        #     heapq.heappush(l,(temp,num))
        # ans = float("inf")
        # while len(l) == len(nums):
        #     # current possible smallest number in the list
        #     low, upp = heapq.heappop(l)
        #     ans = min(ans, max_min - low)
        #     if low % 2 == 1 or low < upp:
        #         low *= 2
        #         max_min = max(max_min, low)
        #         heapq.heappush(l,(low, upp))
        # return ans
