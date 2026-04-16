# [Python/Java/Go] 动态规划 or 双指针

> Author: Benhao
> Date: 2021-08-09
> Upvotes: 20
> Tags: Go, Java, Python, Python3

---

### 解题思路
Happy Birthday~!
<br>
一个等差序列序列，两两相邻的差相等。那么就有两种思路，一种是我们统计当前的数和上一个数的差是否和上一个数和上上个数的差一样，如果一样，说明当前的数和上一个数还有上一个数就构成一个等差数列，而如果上个数和上上个数以前还构成其他等差数列，当前的数和这些等差数列也能构成新的等差数列。也就是说，如果上一个数能构成长度为k的等差数列，那么当前的数就能够构成长度为k+1的等差数列
。而之前的k个序列，从任意一个数开始到当前的数都是等差，所以其中长度大于等于3的都可以作为一个答案(且唯一)。

另一个思路就是我们按某一个固定差，找它构成的最长长度的等差数列是多长，比如说长度为k，那么其中能构成答案的就是长度为k的数组构成的长度为3及以上的子数组数量。长度为3的数量为:k-2,长度为4的数量为k-3,...。其结果为这个求和式子:$1+2+3+\dots+k-2 = (k-1)*(k-2)/2$。

第一个思路实际上就是这个求和公式展开了一个一个叠加的罢了。


### 代码

```Python3 []
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        # 上一个差值
        last = None
        # 上一个差值相同的长度
        last_len = ans = 0
        for i in range(1, n):
            # 相等，差值相同长度加一
            if nums[i] - nums[i-1] == last:
                last_len += 1
            # 否则差值相同长度仅有刚刚这俩的差
            else:
                last_len = 1
            # 从头到尾一共能构成len-1种
            ans += last_len - 1
            last = nums[i] - nums[i-1]
        return ans
```
```Java []
class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int n = nums.length, last_len = 0, ans = 0, last = 2001;
        for(int i=1;i<n;i++){
            if(nums[i]-nums[i-1] == last)
                last_len++;
            else
                last_len = 1;
            ans += last_len - 1;
            last = nums[i] - nums[i-1];
        }
        return ans;
    }
}
```
```Go []
func numberOfArithmeticSlices(nums []int) (ans int) {
    if len(nums) <= 2 {
        return 0
    }
    d, l := nums[1] - nums[0], 0
    for i, num := range nums[2:] {
        if nd := num - nums[i + 1]; nd == d {
            l++
            ans += l
        } else {
            d = nd
            l = 0
        }
    }
    return
}
```

思路二
```Python3 []
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        l = r = ans = 0
        # l = n-2 剩余长度不足以再构成一个等差数列
        while l < n - 2:
            d = nums[l + 1] - nums[l]
            while r < n - 1 and nums[r + 1] - nums[r] == d:
                r += 1
            # k = r - l + 1, (k-1)*(k-2)/2 = (r-l) * (r-l-1)/2
            ans += (r-l) *(r-l-1)//2
            l = r
        return ans
```
```Java []
class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        int n = nums.length, ans = 0;
        for(int l=0,r=0;l < n - 2;){
            int d = nums[l+1] - nums[l];
            while(r < n - 1 && nums[r+1] - nums[r] == d)
                r++;
            ans += (r-l) * (r-l-1) / 2;
            l = r;
        }
        return ans;
    }
}
```
