# [Python/Java/JavaScript/Go] 深度优先搜索

> slug: pythonjavajavascriptgo-shen-du-you-xian-hm3mw
> date: 2022-03-10
> tags: Go, Java, JavaScript, Python, Python3
> question: Count Nodes With the Highest Score (count-nodes-with-the-highest-score)
> url: https://leetcode.cn/problems/count-nodes-with-the-highest-score/solutions/8dBZAF/pythonjavajavascriptgo-shen-du-you-xian-hm3mw/

---
### 解题思路

总共有$n$个节点
对于任意节点$i$，它的分数可以由左子树大小$left_i$和右子树大小$right_i$得到:
$score_i = left_i * right_i * (n - left_i - right_i - 1)$
在这个式子中，乘法项不足1的看作1

这和深度优先搜索是契合的，我们先递归完子节点得到子树的大小，再以递归结果计算当前节点的最终值。

### 代码

```Python3 []
class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        graph = defaultdict(list)
        for i, p in enumerate(parents[1:], 1):
            graph[p].append(i)
        max_score, ans = 0, 0

        def dfs(node):
            left = dfs(graph[node][0]) if graph[node] else 0
            right = dfs(graph[node][1]) if len(graph[node]) == 2 else 0
            nonlocal max_score, ans
            if (score := max(1, (n - left - right - 1)) * max(1, left) * max(1, right)) > max_score:
                max_score, ans = score, 1
            elif score == max_score:
                ans += 1
            return left + right + 1
        
        dfs(0)
        return ans
```
```Java []
class Solution {
    private int ans, n;
    private long maxScore;
    private Map<Integer, List<Integer>> graph;
    public int countHighestScoreNodes(int[] parents) {
        maxScore = ans = 0;
        n = parents.length;
        graph = new HashMap<>();
        for(int i = 1; i < n; i++) {
            List<Integer> list = graph.getOrDefault(parents[i], new ArrayList<>());
            list.add(i);
            graph.put(parents[i], list);
        }
        dfs(0);
        return ans;
    }

    private int dfs(int node) {
        int left, right;
        if(graph.containsKey(node)) {
            List<Integer> list = graph.get(node);
            left = dfs(list.get(0));
            right = list.size() > 1 ? dfs(list.get(1)) : 0;
        } else {
            left = right = 0;
        }
        long score = (long)Math.max(1, left) * (long)Math.max(1, right) * (long)Math.max(1, n - 1 - left - right);
        if(score > maxScore) {
            maxScore = score;
            ans = 1;
        } else if(score == maxScore)
            ans++;
        return left + right + 1;
    }
}
```
```JavaScript []
/**
 * @param {number[]} parents
 * @return {number}
 */
var countHighestScoreNodes = function(parents) {
    let maxScore = 0n, ans = 0
    const n = parents.length, graph = new Map()
    for(let i = 1; i < n; i++) {
        let cur
        if(graph.has(parents[i]))
            cur = graph.get(parents[i])
        else
            cur = new Array()
        cur.push(i)
        graph.set(parents[i], cur)
    }

    dfs = function(node) {
        let left = 0, right = 0
        if(graph.has(node)) {
            const children = graph.get(node)
            left = dfs(children[0])
            right = children.length > 1 ? dfs(children[1]) : 0
        }
        const score = BigInt(Math.max(1, left)) * BigInt(Math.max(1, right)) * BigInt(Math.max(1, n - 1 - left - right))
        if(score > maxScore) {
            maxScore = score
            ans = 1
        } else if(score == maxScore)
            ans++
        return left + right + 1
    }

    dfs(0)
    return ans
};
```
```Go []
func countHighestScoreNodes(parents []int) (ans int) {
    maxScore, n, graph := int64(0), len(parents), map[int][]int{}
    for i := 1; i < n; i++ {
        graph[parents[i]] = append(graph[parents[i]], i)
    }

    var dfs func(node int) int
    dfs = func(node int) int {
        left, right := 0, 0
        children := graph[node]
        if len(children) > 0 {
            left = dfs(children[0])
            if len(children) > 1 {
                right = dfs(children[1])
            }
        }
        if score := max(left, 1) * max(right, 1) * max(n - 1 - left - right, 1); score > maxScore {
            maxScore, ans = score, 1
        } else if score == maxScore {
            ans++
        }
        return left + right + 1
    }
    dfs(0)
    return ans
}

func max(a, b int) int64 {
    if a > b {
        return int64(a)
    }
    return int64(b)
}
```
