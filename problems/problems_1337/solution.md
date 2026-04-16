# [Python/Java] 重拳出击

> Author: Benhao
> Date: 2021-07-31
> Upvotes: 24
> Tags: Python, Python3

---

```Python3 []
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted([i for i in range(len(mat))], key=lambda x:sum(mat[x]))[:k]
```
```Java []
class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {
        int[] ans = new int[k];
        List<Integer> lines = new ArrayList<>();
        for(int i=0;i<mat.length;i++)
            lines.add(binarySearch(mat[i])*100+i);
        Collections.sort(lines);
        for(int i=0;i<k;i++)
            ans[i] = lines.get(i) % 100;
        return ans;
    }

    public int binarySearch(int[] nums){
        int left = 0, right = nums.length;
        while(left < right){
            int mid = left + (right - left)/2;
            if(nums[mid]==0){
                right = mid;
            }else{
                left = mid + 1;
            }
        }
        return left;
    }
}
```