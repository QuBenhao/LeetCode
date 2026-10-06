import solution
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countTriplets(list(test_input))

    def countTriplets(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # hashmap = defaultdict(list)
        # ans = 0
        # for j, num in enumerate(arr):
        #     new = defaultdict(list)
        #     for key, val in hashmap.items():
        #         # If hashmap has a key equal to the current num, their XOR is 0,
        #         # and any index between them except the leftmost is a valid right boundary
        #         if key == num:
        #             ans += j * len(val) - sum(val)
        #         new[num ^ key] = val
        #     new[num].append(j)
        #     hashmap = new
        # return ans

        l, s = Counter(), Counter()
        prexor = ans = 0
        for k, num in enumerate(arr):
            # Update the previous XOR results
            l[prexor] += 1
            s[prexor] += k
            # curxor = arr[0] ^ arr[1] ^ ... ^ arr[k]
            prexor ^= num
            # An earlier i satisfies arr[0] ^ arr[1] ^ ... ^ arr[i] = curxor,
            # so i to k gives an interval with XOR 0, and any index between them except i can serve as j
            if prexor in l:
                # As in the two-loop solution above, use the count and index distances to update the answer
                ans += k * l[prexor] - s[prexor]
        return ans
