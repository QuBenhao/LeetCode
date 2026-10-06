# [Python/Java/JavaScript/Go] Recursion or iteration

> slug: pythonjavajavascriptgo-di-gui-or-die-dai-8yxr
> date: 2022-02-19
> tags: Go, Java, JavaScript, Python, Python3
> question: Pancake Sorting (pancake-sorting)
> url: https://leetcode.cn/problems/pancake-sorting/solutions/WwN8JI/pythonjavajavascriptgo-di-gui-or-die-dai-8yxr/

---
### Approach
Each pancake flip affects the left portion but leaves the unselected right portion unchanged. Sort the rightmost values first, then solve the remaining left portion as a subproblem.

At most two flips move the current maximum to the far right: first flip it to the far left, then flip it into its final position.
For example, with [3,2,4,1], first flip `4` to the front, giving [4,2,3,1], then flip it to the end, giving [1,3,2,4].
Now only [1,3,2] remains to be solved.
This uses at most `2 * arr.length` flips, satisfying the requirement.

### Code

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
