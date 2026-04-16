# [Python/Java] 不知道怎么吐槽了…祝大家七夕快乐吧

> Author: Benhao
> Date: 2021-08-13
> Upvotes: 21
> Tags: Java, Python, Python3

---

### 解题思路
摘了一下诺手的话，看完能看懂题了起码[@zbtzbt](/u/zbtzbt/)

就是暴力模拟，判断有没有不开心……
我不想优化了，今天我就非得多用一些对象（没有对象还不能new了吗？？）。


希望七夕不快乐的朋友--！快乐++!

### 代码

```python3
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        """
        之前男生x和女生u是一对，轰轰烈烈的爱了一场，但是迫于生活和现实，分手走散了。
        若干年后，x在前女友u的婚礼上，男生x发现，自己迫于无奈找了一个不太爱的人y；
        而前女友u也找了一个不太爱的人v。男生x酒后痛哭，觉得非常难过，我们最终还是败给了现实。
        """
        mark = [[0] * n for _ in range(n)]
        for i, pref in enumerate(preferences):
            cur = n - 1
            for people in pref:
                mark[i][people] = cur
                cur -= 1
        ans = set()

        for i in range(len(pairs)):
            for j in range(i):
                x, y = pairs[i]
                u, v = pairs[j]
                if mark[x][y] < mark[x][u] and mark[u][v] < mark[u][x]:
                    ans.add(u)
                    ans.add(x)
                if mark[y][x] < mark[y][u] and mark[u][v] < mark[u][y]:
                    ans.add(u)
                    ans.add(y)
                if mark[x][y] < mark[x][v] and mark[v][u] < mark[v][x]:
                    ans.add(v)
                    ans.add(x)
                if mark[y][x] < mark[y][v] and mark[v][u] < mark[v][y]:
                    ans.add(v)
                    ans.add(y)
        return len(ans)
```
另一种写法
```Python3 []
class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        mark = [[0] * n for _ in range(n)]
        for i, pref in enumerate(preferences):
            for j, lover in enumerate(pref):
                mark[i][lover] = j

        couple = dict()
        for a,b in pairs:
            couple[a] = b
            couple[b] = a

        ans = 0
        for x in range(n):
            y = couple[x]
            for u in range(n):
                if u == x or u == y:
                    continue
                v = couple[u]
                if mark[x][y] > mark[x][u] and mark[u][v] > mark[u][x]:
                    ans += 1
                    break
        return ans
```
```Java []
class Solution {
    public int unhappyFriends(int n, int[][] preferences, int[][] pairs) {
        int[][] score = new int[n][n];
        for(int i=0;i<n;i++)
            for(int j=0;j<n-1;j++)
                score[i][preferences[i][j]] = j;
        
        Map<Integer, Integer> lover = new HashMap<>();
        for(int i=0;i<pairs.length;i++){
            int a = pairs[i][0], b = pairs[i][1];
            lover.put(a, b);
            lover.put(b, a);
        }
        
        int ans = 0;
        for(int i=0;i<n;i++){
            int y = lover.get(i);
            for(int j=0;j<n;j++){
                if(j == i || j == y)
                    continue;
                int v = lover.get(j);
                if(score[i][y] > score[i][j] && score[j][v] > score[j][i]){
                    ans++;
                    break;
                }
            }
        }
        return ans;
    }
}
```

### 复杂度
时间复杂度$o(n^2)$
空间复杂度$o(n^2)$