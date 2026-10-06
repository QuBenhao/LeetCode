# [Python/Java/JavaScript/Go] Binary search

> Author: Benhao
> Date: 2022-02-13
> Upvotes: 19
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
According to the problem, the array should have pairs such as `nums[0] == nums[1]` and `nums[2] == nums[3]`, or generally `nums[i] == nums[i^1]`.
If the pair does not match, the split point lies to its left and has shifted the pairing. If it matches, the split point lies to its right, so the pairing has not shifted yet.
If `nums[mid] == nums[mid^1]`, set `left = mid + 1`; otherwise, set `right = mid`.


The [Python3.10](https://docs.python.org/zh-cn/3/library/bisect.html#module-bisect) documentation describes key as follows: 指定带有单个参数的 key function，用于从每个输入元素中提取比较键。 默认值为 None (直接比较元素)。(Here, set x to True and the key function to nums[x] != nums[x ^ 1].)
[bisect source reference](https://github.com/python/cpython/blob/3.10/Lib/bisect.py)

If setting x to True in Python's bisect is hard to follow, here is another way to view the problem.
Under the key function `lambda x: nums[x] != nums[x ^ 1]`, the original array [1,1,2,3,3,4,4,8,8] can be viewed as [False, False, True, True, True, True, True, True, True].
We want the position of the first True, which is the left insertion point for True.

### Code

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
        # Equivalent versions using bisect_right and bisect_left
        return nums[bisect_right(range(len(nums) - 1), False, key=lambda x: nums[x] != nums[x ^ 1])]
```
