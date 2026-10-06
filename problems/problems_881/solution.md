# [Python] Greedy sorting + two pointers

> Author: Benhao
> Date: 2021-08-25
> Upvotes: 20
> Tags: Java, Python, Python3

---

### Approach
Observe that heavier people are more likely to need a boat to themselves. To use space efficiently, pair them with someone whenever possible.

> If the heaviest person cannot share even with the lightest, they must take a boat alone. Solve the remaining problem recursively;
> If the heaviest can take the lightest, pairing them is optimal: the lightest can share with anyone, but others may not fit with the heaviest.

Sort and use two pointers. If their combined weight is at most limit, pair the left and right people and continue inward; otherwise, the rightmost person takes a boat alone.

### Code

```Python3 []
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        left, right = 0, n - 1
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            ans += 1
        return ans
```
```Java []
class Solution {
    public int numRescueBoats(int[] people, int limit) {
        Arrays.sort(people);
        int n = people.length, ans = 0;
        for(int left=0,right=n-1;left<=right;ans++)
            if(people[left] + people[right--] <= limit)
                left++;
        return ans;
    }
}
```
