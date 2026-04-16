# [Python] 贪心 排序+双指针

> Author: Benhao
> Date: 2021-08-25
> Upvotes: 20
> Tags: Java, Python, Python3

---

### 解题思路
观察这么一件事儿，越重的人，越容易自己独占一条船。如果想尽可能地利用空间，就尽可能往它们上面塞人。

> 如果最重的，重到连最轻的都加不上去，那它只能自己一个人一条船。剩下的问题就是一个递归的解了;
> 如果最重的可以带上最轻的，那它们俩一艘船是最优的。因为最轻的能和任一个人一起，但其他人不一定能和最重的人一起。

排序后，双指针。如果两人的和小于等于limit，那么左右凑一对儿，往中间递归；否则右边独自占一条船。

### 代码

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