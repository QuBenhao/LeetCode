# [Python/Java/TypeScript/Go] Tian Ji's horse-racing strategy

> slug: pythonjavatypescriptgo-tianjisaimai-by-h-u4h8
> date: 2022-10-08
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Advantage Shuffle (advantage-shuffle)
> url: https://leetcode.cn/problems/advantage-shuffle/solutions/YeLz0J/pythonjavatypescriptgo-tianjisaimai-by-h-u4h8/

---
### Approach
If the largest number in nums2 is at least the largest in nums1, that number is unbeatable.
Thus nums1 can have an advantage at at most one fewer than its total number of positions.
Since we must give up this position, assign our smallest number to it.
Otherwise, match the largest number in nums1 against the largest in nums2.
Solve the remaining numbers recursively.

### Code

```Python3 []
class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        n = len(nums1)
        ans, left, right = [-1] * n, 0, n - 1
        for idx in sorted(range(n), key=lambda x:-nums2[x]):
            if nums2[idx] >= nums1[right]:
                ans[idx] = nums1[left]
                left += 1
            else:
                ans[idx] = nums1[right]
                right -= 1
        return ans
```
```Java []
class Solution {
    public int[] advantageCount(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        int n = nums1.length;
        Integer[] idxs = new Integer[n];
        for (int i = 0; i < n; i++) {
            idxs[i] = i;
        }
        Arrays.sort(idxs, (a, b) -> nums2[b] - nums2[a]);
        int left = 0, right = n - 1;
        int[] ans = new int[n];
        for (int idx: idxs) {
            if (nums2[idx] >= nums1[right]) {
                ans[idx] = nums1[left++];
            } else {
                ans[idx] = nums1[right--];
            }
        }
        return ans;
    }
}
```
```TypeScript []
function advantageCount(nums1: number[], nums2: number[]): number[] {
    const n: number = nums1.length, ans: Array<number> = new Array<number>(n).fill(-1)
    const idxs: Array<number> = new Array<number>(n).fill(0).map((_, index) => index).sort((a, b) => nums2[b] - nums2[a])
    nums1.sort((a, b) => a - b)
    let left: number = 0, right: number = n - 1
    for (const idx of idxs) {
        if (nums2[idx] >= nums1[right]) {
            ans[idx] = nums1[left++]
        } else {
            ans[idx] = nums1[right--]
        }
    }
    return ans
};
```
```Go []
func advantageCount(nums1 []int, nums2 []int) []int {
    n := len(nums1)
    sort.Ints(nums1)
    ans, idxs := make([]int, n), make([]int, n)
    for i := 0; i < n; i++ {
        idxs[i] = i
    }
    sort.Slice(idxs, func(i, j int) bool { return nums2[idxs[i]] > nums2[idxs[j]] })
    left, right := 0, n - 1
    for _, idx := range idxs {
        if nums2[idx] >= nums1[right] {
            ans[idx] = nums1[left]
            left++
        } else {
            ans[idx] = nums1[right]
            right--
        }
    }
    return ans
}
```
