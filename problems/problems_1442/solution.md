# [Python] From two loops to one

> Author: Benhao
> Date: 2021-05-18
> Upvotes: 6
> Tags: Python, Python3

---

### Approach
**Key insight**
Observe that when `2^3 = 1`, we also have `2 = 3^1`.
In other words, `a^b^c = d` also implies `a^b = c^d` and `a = b^c^d`.
For `i,k` satisfying `arr[i] ^ arr[i+1] ^ ... ^ arr[k] = 0`, every `j` in `[i+1,k]` forms a valid triplet.
There are `k-i` choices in `[i+1,k]`, so the pair `i,k` contributes `k-i` valid values of j.

Track all previous XOR sums (the XOR of each interval through the preceding array element). When one equals the current value, we need to know `which indices have an XOR value equal to the current value`.
If we store the indices whose XOR value is `m` in a list, `len(list) * k - sum(list)` gives the contribution of all triplets with right boundary `k`.

**From two loops to one**
Tracking all XOR sums from the previous iteration is another prefix-XOR problem, since `num[i] ^ num[i+1] ^ ... num[k-1] = prexor[i] ^ prexor[k]`.
If some prexor[i] equals the current XOR result, we have found a pair `i,k`. Recording all `i` satisfying `prexor[i] = prexor[k]` allows the update above.

### Code

```python3
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # hashmap = defaultdict(list)
        # ans = 0
        # for j, num in enumerate(arr):
        #     new = defaultdict(list)
        #     for key, val in hashmap.items():
        #         # A key in hashmap equal to the current num gives a valid interval,
        #         # and any index in it except the leftmost can serve as j
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

```
