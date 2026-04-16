# [Python/Java/JavaScript/Go] 二分查找

> Author: Benhao
> Date: 2022-02-13
> Upvotes: 19
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
根据题目描述，数组应该呈现为`nums[0] == nums[1]`, `nums[2] == nums[3]`的形式，也就是`nums[i] == nums[i^1]`
如果不相等，那么说明分割点在该点左边，导致了错位；如果相等，说明分割点在该点右边，还没有错位。
也就是如果`nums[mid] == nums[mid^1]`，我们要`left = mid + 1`；否则我们要`right = mid`


[Python3.10](https://docs.python.org/zh-cn/3/library/bisect.html#module-bisect)中使用key 指定带有单个参数的 key function，用于从每个输入元素中提取比较键。 默认值为 None (直接比较元素)。（转换一下x为True, key function为nums[x] != nums[x ^ 1]）
[bisect源码参考](https://github.com/python/cpython/blob/3.10/Lib/bisect.py)

对于Python的bisect中的x设为True不好理解的话，我将题目翻译一下，
原数组[1,1,2,3,3,4,4,8,8]在key function `lambda x: nums[x] != nums[x ^ 1]`下可以看做是[False, False, True, True, True, True, True, True, True]
我们要找第一个True的位置（左插一个True）

### 代码

```Python3 []
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return nums[bisect_left(range(len(nums) - 1), True, key=lambda x: nums[x] != nums[x ^ 1])]
```
```Java []
class Solution {
    public int singleNonDuplicate(int[] nums) {
        int left = 0, right = nums.length - 1;
        while(left < right) {
            int mid = (left + right) / 2;
            if(nums[mid] == nums[mid ^ 1])
                left = mid + 1;
            else
                right = mid;
        }
        return nums[left];
    }
}
```
```JavaScript []
/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNonDuplicate = function(nums) {
    let left = 0, right = nums.length - 1
    while(left < right) {
        const mid = Math.floor((left + right) / 2)
        if(nums[mid] == nums[mid ^ 1])
            left = mid + 1
        else
            right = mid
    }
    return nums[left]
};
```
```Go []
func singleNonDuplicate(nums []int) int {
    l := 0
    for r := len(nums) - 1; l < r; {
        mid := (l + r) / 2
        if nums[mid] == nums[mid ^ 1] {
            l = mid + 1
        } else {
            r = mid
        }
    }
    return nums[l]
}
```

```python3
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # bisect_right和bisect_left等价写法
        return nums[bisect_right(range(len(nums) - 1), False, key=lambda x: nums[x] != nums[x ^ 1])]
```