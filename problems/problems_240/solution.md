# [Python/Java/JavaScript] A BST rooted at the bottom-left or top-right corner

> Author: Benhao
> Date: 2021-10-24
> Upvotes: 14
> Tags: Java, JavaScript, Python, Python3

---

### Approach
With the bottom-left or top-right corner as the root, the entire matrix can be viewed as a binary search tree.

### Code

```Python3 []
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False
```
```Java []
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length, n = matrix[0].length;
        for(int i=m-1,j=0;i>=0&&j<n;){
            if(matrix[i][j] == target)
                return true;
            else if(matrix[i][j] < target)
                j += 1;
            else
                i -= 1;
        }
        return false;
    }
}
```
```JavaScript []
/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var searchMatrix = function(matrix, target) {
    const m = matrix.length, n = matrix[0].length;
    for(let i=m-1,j=0;i>=0&&j<n;){
        if(matrix[i][j] == target)
            return true;
        else if(matrix[i][j] < target)
            j += 1;
        else
            i -= 1;
    }
    return false;
};
```

Also included is a binary search solution I wrote earlier.
```Python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def findColumnRange(): 
            for y in range(m): 
                if matrix[y][0] > target: 
                    return y-1
            return m-1
        
        def binarySearch(y): 
            left = 0
            right = n-1 
            while left <= right: 
                mid = (left + right)//2
                if matrix[y][mid] == target: 
                    return True 
                elif matrix[y][mid] > target: 
                    right = mid - 1 
                else: 
                    left = mid + 1
            return False

        m, n = len(matrix), len(matrix[0])
        for y in range(findColumnRange()+1):
            if binarySearch(y):
                return True
        return False
```
