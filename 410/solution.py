import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, m = test_input
        return self.splitArray(list(nums), m)

    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        # Checks to see if x is a valid possibility given the constraint of m subarrays
        def isPossible(limit, nums, m):
            numSubarrays = 1
            subarraySum = 0
            for num in nums:
                # Greedily try to add this element to the current subarray as long as the sub_array's sum doesn't exceed
                # our upper limit x
                if (num + subarraySum) <= limit:
                    subarraySum += num
                # If sum would be exceeded by adding the current element, we need to start a new subarray and put this
                # element into that
                else:
                    numSubarrays += 1
                    subarraySum = num

            return numSubarrays <= m

        # First, understand WHAT we are binary searching over
        # we are doing a binary search over the *search space of possible results*
        # What is the search space, aka what are all possible results?
        # For this, we need to know the minimum and maximum possible result
        # minimum possible result - largest element in array. Since each element needs
        # to be part of some subarray, the smallest we can go is by taking the largest element
        # in a subarray by itself
        # maximum possible result - sum of all elements in the array since we cannot form
        # a subarray larger than the array itself
        # Compute minResult and maxResult boundaries
        minResult, maxResult = 0, 0
        for num in nums:
            maxResult += num
            if num > minResult:
                minResult = num

        # now that we have our minResult and maxResult boundaries, we can begin searching within this space What are
        # we searching for? The smallest value within this space such that we can form m subarrays from nums and none
        # of their sums exceed that value
        finalResult = float('inf')
        while minResult <= maxResult:
            # Start by checking if the value in the middle of the search space satisfies this desired outcome
            # If it does, we can discard all values to the right of this in our search space since we have
            # something better than those already. We only need to search values to the left to see if
            # we can find something better
            # If not, we only need to search values higher than mid
            mid = (minResult + maxResult) // 2
            if isPossible(mid, nums, m):
                finalResult = mid
                maxResult = mid - 1
            else:
                minResult = mid + 1

        return finalResult
