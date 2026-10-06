# [Python/Java/JavaScript/Go] Inorder traversal + merge (advanced: inorder iterators + merge)

> slug: python-by-himymben-1zz0
> date: 2022-04-30
> tags: Go, Java, JavaScript, Python, Python3
> question: All Elements in Two Binary Search Trees (all-elements-in-two-binary-search-trees)
> url: https://leetcode.cn/problems/all-elements-in-two-binary-search-trees/solutions/PZ44ds/python-by-himymben-1zz0/

---
### Approach
The input trees are binary search trees, so inorder traversal directly produces sorted lists.
The problem becomes merging two sorted lists.
Compare the current values in the two arrays, append the smaller value to the answer, and advance its pointer.

The iterator version follows the same approach, but retrieves only the next smallest value for comparison instead of generating the full list at once. This has a large advantage when the trees are large but only a small portion of the merged result is needed.

PS:
I am not sure why the iterator version is so slow; could someone explain?

### Code

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root, res):
            if root:
                dfs(root.left, res)
                res.append(root.val)
                dfs(root.right, res)
        
        ans, nums1, nums2 = [], [], []
        dfs(root1, nums1), dfs(root2, nums2)
        idx1 = idx2 = 0
        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] <= nums2[idx2]:
                ans.append(nums1[idx1])
                idx1 += 1
            else:
                ans.append(nums2[idx2])
                idx2 += 1
        ans.extend(nums1[idx1:] + nums2[idx2:])
        return ans
```
```Java []
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> nums1 = new ArrayList<>(), nums2 = new ArrayList<>(), ans = new ArrayList<>();
        inOrderTraverse(root1, nums1);
        inOrderTraverse(root2, nums2);
        int idx1 = 0, idx2 = 0;
        while(idx1 < nums1.size() && idx2 < nums2.size()) {
            if(nums1.get(idx1) <= nums2.get(idx2))
                ans.add(nums1.get(idx1++));
            else
                ans.add(nums2.get(idx2++));
        }
        while(idx1 < nums1.size())
            ans.add(nums1.get(idx1++));
        while(idx2 < nums2.size())
            ans.add(nums2.get(idx2++));
        return ans;
    }

    private void inOrderTraverse(TreeNode node, List<Integer> list) {
        if(node != null) {
            inOrderTraverse(node.left, list);
            list.add(node.val);
            inOrderTraverse(node.right, list);
        }
    }
}
```
```JavaScript []
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @return {number[]}
 */
var getAllElements = function(root1, root2) {
    const inOrderTraverse = function(root, nums) {
        if(root != null) {
            inOrderTraverse(root.left, nums)
            nums.push(root.val)
            inOrderTraverse(root.right, nums)
        }
    }
    const ans = new Array(), nums1 = new Array(), nums2 = new Array()
    inOrderTraverse(root1, nums1)
    inOrderTraverse(root2, nums2)
    let idx1 = 0, idx2 = 0
    while(idx1 < nums1.length && idx2 < nums2.length)
        if(nums1[idx1] <= nums2[idx2])
            ans.push(nums1[idx1++])
        else
            ans.push(nums2[idx2++])
    while(idx1 < nums1.length)
        ans.push(nums1[idx1++])
    while(idx2 < nums2.length)
        ans.push(nums2[idx2++])
    return ans
};
```
```Go []
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func getAllElements(root1 *TreeNode, root2 *TreeNode) []int {
    inOrderTraverse := func(root *TreeNode) (nums []int) {
        var dfs func(*TreeNode)
        dfs = func(node *TreeNode) {
            if node != nil {
                dfs(node.Left)
                nums = append(nums, node.Val)
                dfs(node.Right)
            }
        }
        dfs(root)
        return
    }

    ans, nums1, nums2 := []int{}, inOrderTraverse(root1), inOrderTraverse(root2)
    idx1, idx2 := 0, 0
    for idx1 < len(nums1) && idx2 < len(nums2) {
        if nums1[idx1] <= nums2[idx2] {
            ans = append(ans, nums1[idx1])
            idx1++
        } else {
            ans = append(ans, nums2[idx2])
            idx2++
        }
    }
    for idx1 < len(nums1) {
        ans = append(ans, nums1[idx1])
        idx1++
    }
    for idx2 < len(nums2) {
        ans = append(ans, nums2[idx2])
        idx2++        
    }
    return ans
}
```

```python3 [v1 - First iterator approach]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root):
            if root:
                yield from dfs(root.left)
                yield root.val
                yield from dfs(root.right)
        
        ans, a, b = [], None, None
        gen1, gen2 = dfs(root1), dfs(root2)
        while True:
            try:
                if a is None:
                    a = next(gen1)
                if b is None:
                    b = next(gen2)
                if a < b:
                    ans.append(a)
                    a = None
                else:
                    ans.append(b)
                    b = None
            except StopIteration:
                break
        if a is not None:
            ans.append(a)
        if b is not None:
            ans.append(b)
        ans.extend(chain(gen1, gen2))
        return ans
```
```Python3 [v1 - Second iterator approach]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(root):
            if root:
                yield from dfs(root.left)
                yield root.val
                yield from dfs(root.right)
        
        ans = []
        gen1, gen2 = dfs(root1), dfs(root2)
        a, b = next(gen1, None), next(gen2, None)
        while a is not None and b is not None:
            if a < b:
                ans.append(a)
                a = next(gen1, None)
            else:
                ans.append(b)
                b = next(gen2, None)
        if a is not None:
            ans.append(a)
        if b is not None:
            ans.append(b)
        ans.extend(chain(gen1, gen2))
        return ans
```
