# [Python/Java] 容斥原理 时间o(n) 空间o(1)

> Author: Benhao
> Date: 2021-08-28
> Upvotes: 26
> Tags: Java, Python, Python3

---

### 解题思路
首先把问题转化成，每个数存在在多少个奇数子数组中，也就是每个数重复了多少次。很容易发现第一个数，重复的次数由总长决定。奇数的子数组有多少个呢，正好是`(length + 1) // 2`。
那么前一个数和后一个数是否存在依赖关系呢？
观察到，第一个数组成长度3、5、7等长度的子数组的时候，始终带着第二个数，但长度为1的时候没有第二个数出现。
同样的，从第二个数往后面组成的子数组和第一个数没有关系。
也就是说，第二个数出现了`第一个数出现的次数`，但是少了`第一个数出现、第二个数没出现的次数`。而且第二个数还比第一个数多了`第二个数出现、第一个数没出现的次数`。
上一个数出现的次数可以记录。
那么上一个数出现，当前的数没出现有多少次呢？正好是一个递归思想,数组从0到i-1构成多少个包含i-1的子数组，就又是长度计算的。
而当前的数出现，上一个数没出现，又正好是i到n-1构成多少个包含i的子数组，同样是长度计算的。

于是我们知道以下信息:
> 第一位出现(n+1)//2次
> 当前位比上一位多 (n - i + 1) // 2 - (i + 1) // 2
> 首尾对应位置出现次数相同(对称性)

另外，不用双指针按这个规律从头遍历到尾也不是不行哈。

### 代码

```Python3 []
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # 长度为n的数组，第一位出现在多少个奇数长度的子数组？
        # 1, 3, 5, ..., length-1/length
        # (length + 1)//2
        n = len(arr)
        l, r, ans, times = 0, n - 1, 0, (n+1) // 2
        while l <= r:
            # 对称性，前后对称位置出现的次数一样
            if l < r:
                ans += times * (arr[l] + arr[r])
            else:
                ans += times * arr[l]
            l += 1
            r -= 1
            # 下一个数比前一个数多了后一个数构成的不带前一个数的奇数子数组的个数
            times += (n - l + 1) // 2 
            # 下一个数比前一个数少了前一个数构成的不带后一个数的奇数子数组的个数
            times -= (l + 1) // 2
        return ans
```
```Java []
class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int n = arr.length;
        int ans = 0;
        for(int l = 0, r = n - 1, times = (n + 1)/2; l<=r; r--){
            if(l < r)
                ans += times * (arr[l] + arr[r]);
            else
                ans += times * arr[l];
            times += (n-++l+1)/2 - (l+1)/2;
        }
        return ans;
    }
}
```