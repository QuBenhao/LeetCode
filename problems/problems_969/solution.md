# [Python/Java/JavaScript/Go] 递归 or 迭代

> slug: pythonjavajavascriptgo-di-gui-or-die-dai-8yxr
> date: 2022-02-19
> tags: Go, Java, JavaScript, Python, Python3
> question: Pancake Sorting (pancake-sorting)
> url: https://leetcode.cn/problems/pancake-sorting/solutions/WwN8JI/pythonjavajavascriptgo-di-gui-or-die-dai-8yxr/

---
### 解题思路
由于煎饼排序每次都会影响到左边，而不会影响到没被选择的右边，那么我们优先排序右边的值，这样再去解决左边的值就是解决子问题了。

注意到最多花两次，就可以将当前最大值移动到最右边。（第一次将最大值翻到最左边，第二次翻到它的位置即可）
比如[3,2,4,1]首先将`4`翻到第一个，即[4,2,3,1]，再将起翻到最后一个，也就是[1,3,2,4]。
那么接下来我们只需对[1,3,2]求解即可。
而这样翻转最多使用`2 * arr.length`次，满足题目要求。

### 代码

```Python3 []
class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        return (([idx + 1, len(arr)] if idx else [len(arr)]) + self.pancakeSort(arr[idx+1:][::-1] + arr[:idx]) if (idx := arr.index(len(arr))) < len(arr) - 1 else self.pancakeSort(arr[:idx])) if arr else []
```
```Java []
class Solution {
    public List<Integer> pancakeSort(int[] arr) {
        List<Integer> ans = new ArrayList<>();
        for(int i = arr.length - 1; i > 0; i--) {
            int j = i;
            for(; j > 0; j--)
                if(arr[j] == i + 1)
                    break;
            if(j < i) {
                if(j > 0) {
                    ans.add(j + 1);
                    reverse(arr, j);
                }
                ans.add(i + 1);
                reverse(arr, i);
            }
        }
        return ans;
    }

    private void swap(int[] arr, int i, int j) {
        int tmp = arr[i];
        arr[i] = arr[j];
        arr[j] = tmp;
    }

    private void reverse(int[] arr, int len) {
        for(int i = 0, j = len; i < j; i++)
            swap(arr, i, j--);
    }
}
```
```JavaScript []
/**
 * @param {number[]} arr
 * @return {number[]}
 */
var pancakeSort = function(arr) {
    swap = function(i, j) {
        const tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
    }

    reverse = function(idx) {
        for(let i = 0, j = idx; i < j; i++)
            swap(i, j--)
    }

    const ans = new Array()
    for(let i = arr.length - 1; i > 0; i--) {
        let j = i;
        for(;j > 0; j--)
            if(arr[j] == i + 1)
                break
        if(j < i) {
            if(j > 0) {
                ans.push(j + 1)
                reverse(j)
            }
            ans.push(i + 1)
            reverse(i)
        }
    }

    return ans
};
```
```Go []
func pancakeSort(arr []int) (ans []int) {
    reverse := func(num []int, idx int) {
        for i, j := 0, idx; i < j; i++ {
            num[i], num[j] = num[j], num[i]
            j--
        }
    }

    for i := len(arr) - 1; i > 0; i-- {
        j := i
        for ; j > 0; j-- {
            if arr[j] == i + 1 {
                break
            }
        }
        if j < i {
            if j > 0 {
                ans = append(ans, j + 1)
                reverse(arr, j)
            }
            ans = append(ans, i + 1)
            reverse(arr, i)
        }
    }
    return
}
```