# 872. Leaf-Similar Trees [Rating: 1287.90]

Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a **leaf value sequence***.*

![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png)

For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.

Two binary trees are considered *leaf-similar* if their leaf value sequence is the same.

Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-1.jpg)

```
Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
```

**Example 2:**

```
Input: root1 = [1], root2 = [1]
Output: true
```

**Example 3:**

```
Input: root1 = [1], root2 = [2]
Output: false
```

**Example 4:**

```
Input: root1 = [1,2], root2 = [2,2]
Output: true
```

**Example 5:**

![img](https://assets.leetcode.com/uploads/2020/09/03/leaf-similar-2.jpg)

```
Input: root1 = [1,2,3], root2 = [1,3,2]
Output: false
```

 

**Constraints:**

- The number of nodes in each tree will be in the range `[1, 200]`.
- Both of the given trees will have values in the range `[0, 200]`.