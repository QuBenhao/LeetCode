# [Python/Java/TypeScript/Go] DFS + 原地标记

> Author: Benhao
> Date: 2022-07-17
> Upvotes: 26
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
题目的意思是按数组坐标的值作为下一个坐标进行转圈，当走到走过的坐标就形成了环，找最大的环。
那么从每个位置开始递归，走过的标记为-1，按原值继续往下走，直到走到一个-1为止。

注意题目没有重复的元素所以不会出现交叉的情况，只有一大堆环。


评论区问了个好问题,
这里统一解释一下`nums[idx], idx = -1, nums[idx]`和`idx, nums[idx] = nums[idx], -1`的区别:
> py里面会先把右边的所有变量的当时的值放到那里。
> 然后左边的值依次赋值。如果你先赋值idx，nums[idx]就不再是你想的那个idx位置了，
> 因为idx变了。它是根据你的idx找的变量而不是自己是一个变量

### 代码

```Python3 []
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def dfs(idx: int) -> int:
            # 走过的位置，环的结尾，返回计算原长度
            if nums[idx] == -1:
                return 0
            # 下一个坐标、标记走过
            nxt, nums[idx] = nums[idx], -1
            return 1 + dfs(nxt)
        
        #  找从某个坐标出发的最大环
        return max(dfs(i) for i in range(len(nums)))
```
```Java []
class Solution {
    public int arrayNesting(int[] nums) {
        int ans = 0;
        for (int i = 0; i < nums.length; i++) {
            ans = Math.max(ans, dfs(nums, i));
        }
        return ans;
    }

    private int dfs(int[] nums, int idx) {
        if (nums[idx] == -1) {
            return 0;
        }
        int nxt = nums[idx];
        nums[idx] = -1;
        return 1 + dfs(nums, nxt);
    }
}
```
```TypeScript []
function arrayNesting(nums: number[]): number {
    const dfs = (idx: number): number => {
        if (nums[idx] == -1) {
            return 0
        }
        let nxt = nums[idx]
        nums[idx] = -1
        return 1 + dfs(nxt)
    }
    let ans = 0
    for (let i = 0; i < nums.length; i++) {
        ans = Math.max(ans, dfs(i))
    }
    return ans
};
```
```Go []
func arrayNesting(nums []int) (ans int) {
    var dfs func (idx int) int
    dfs = func(idx int) int {
        if nums[idx] == -1 {
            return 0
        }
        nxt := nums[idx]
        nums[idx] = -1
        return 1 + dfs(nxt)        
    }
    for i := 0; i < len(nums); i++ {
        if v := dfs(i); v > ans {
            ans = v
        }
    }
    return
}
```

迭代写法
```python3
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            idx, cur = i, 0
            while nums[idx] != -1:
                nums[idx], idx, cur = -1, nums[idx], cur + 1
            ans = max(ans, cur)
        return ans
```