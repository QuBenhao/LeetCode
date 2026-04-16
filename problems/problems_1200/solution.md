# [Python/Java/TypeScript/Go] 排序模拟

> Author: Benhao
> Date: 2022-07-03
> Upvotes: 24
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
排序后所有可能的最小绝对值由每对儿相邻的差构成

### 代码

```Python3 []
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        m, ans = inf, []
        for a, b in pairwise(sorted(arr)):
            if (cur := b - a) < m:
                m, ans = cur, [[a, b]]
            elif cur == m:
                ans.append([a, b])
        return ans
```
```Java []
class Solution {
    public List<List<Integer>> minimumAbsDifference(int[] arr) {
        Arrays.sort(arr);
        List<List<Integer>> list = new ArrayList<>();
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < arr.length - 1; i++) {
            int diff = arr[i + 1] - arr[i];
            if (diff < min) {
                min = diff;
                list.clear();
                List<Integer> cur = new ArrayList<>();
                cur.add(arr[i]);
                cur.add(arr[i + 1]);
                list.add(cur);
            } else if (diff == min) {
                List<Integer> cur = new ArrayList<>();
                cur.add(arr[i]);
                cur.add(arr[i + 1]);
                list.add(cur);
            }
        }
        return list;
    }
}
```
```TypeScript []
function minimumAbsDifference(arr: number[]): number[][] {
    arr.sort((a, b) => a - b)
    let ans = new Array<Array<number>>(), min = Number.MAX_SAFE_INTEGER
    for (let i = 0; i < arr.length - 1; i++) {
        const cur = arr[i + 1] - arr[i]
        if (cur < min) {
            min = cur
            ans = [[arr[i], arr[i + 1]]]
        } else if (cur == min) {
            ans.push([arr[i], arr[i + 1]])
        }
    }
    return ans
};
```
```Go []
func minimumAbsDifference(arr []int) (ans [][]int) {
    sort.Ints(arr)
    for i, min := 0, math.MaxInt32; i < len(arr) - 1; i++ {
        if diff := arr[i + 1] - arr[i]; diff < min {
            min = diff
            ans = [][]int{[]int{arr[i], arr[i + 1]}}
        } else if diff == min {
            ans = append(ans, []int{arr[i], arr[i + 1]})
        }
    }
    return
}
```