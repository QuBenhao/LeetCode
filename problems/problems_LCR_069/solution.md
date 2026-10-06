# [Python/Java/JavaScript] Binary search

> slug: pythonjavajavascript-er-fen-by-himymben-5cau
> date: 2021-10-13
> tags: Java, JavaScript, Python, Python3
> question: 山脉数组的峰顶索引 (B1IidL)
> url: https://leetcode.cn/problems/B1IidL/solutions/rd5wAE/pythonjavajavascript-er-fen-by-himymben-5cau/

---
### Approach
The array is known to be a mountain array. Comparing each element with its neighbors indicates which direction leads to the peak, so use binary search.

### Code

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
