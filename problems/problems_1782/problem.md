# 1782. Count Pairs Of Nodes [Rating: 2457.12]

You are given an undirected graph represented by an integer `n`, which is the number of nodes, and `edges`, where `edges[i] = [ui, vi]` which indicates that there is an undirected edge between `ui` and `vi`. You are also given an integer array `queries`.

The answer to the `jth` query is the number of pairs of nodes `(a, b)` that satisfy the following conditions:

- `a < b`
- `cnt` is **strictly greater** than `queries[j]`, where `cnt` is the number of edges incident to `a` **or** `b`.

Return an array `answers` such that `answers.length == queries.length` and `answers[j]` is the answer of the `jth` query.

Note that there can be **repeated edges**.

 

**Example 1:**

![img](https://assets.leetcode.com/uploads/2021/02/11/screenshot-from-2021-02-11-23-07-35.png)

```
Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
Output: [6,5]
Explanation: The number of edges incident to at least one of each pair is shown above.
```

**Example 2:**

```
Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
Output: [10,10,9,8,6]
```

 

**Constraints:**

- 2 <= n <= 2 * 10<sup>4</sup>
- 1 <= edges.length <= 10<sup>5</sup>
- `1 <= ui, vi <= n`
- `ui != vi`
- `1 <= queries.length <= 20`
- `0 <= queries[j] < edges.length`

