# [Python/Java/JavaScript] 二分

> slug: pythonjavajavascript-er-fen-by-himymben-5cau
> date: 2021-10-13
> tags: Java, JavaScript, Python, Python3
> question: 山脉数组的峰顶索引 (B1IidL)
> url: https://leetcode.cn/problems/B1IidL/solutions/rd5wAE/pythonjavajavascript-er-fen-by-himymben-5cau/

---
### 解题思路
题目已知是个山峰数组了，每个点跟它两边的大小关系，都能告诉我们山峰应该在哪儿，故采取二分。

### 代码

```Python3 []
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l,r = 1,len(arr) - 2
        while l < r:
            mid = (l + r)//2
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] > arr[mid - 1]:
                l = mid + 1
            else:
                r = mid - 1
        return l
```
```Java []
class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int l = 1, r = arr.length - 2;
        while(l < r){
            int mid = (l + r)/2;
            if(arr[mid] > arr[mid-1] && arr[mid] > arr[mid + 1])
                return mid;
            else if(arr[mid] > arr[mid - 1])
                l = mid + 1;
            else
                r = mid - 1;
        }
        return l;
    }
}
```
```JavaScript []
/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function(arr) {
    let l = 1, r = arr.length - 2;
    while(l < r){
        let mid = Math.floor((l + r)/2);
        if(arr[mid] > arr[mid-1] && arr[mid] > arr[mid + 1])
            return mid;
        else if(arr[mid] > arr[mid - 1])
            l = mid + 1;
        else
            r = mid - 1;
    }
    return l;
};
```