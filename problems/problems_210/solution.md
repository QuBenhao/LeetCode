# [Python/Java] 拓扑排序

> Author: Benhao
> Date: 2021-08-05
> Upvotes: 3
> Tags: Java, Python, Python3

---

### 解题思路
和207一致，只是加入了一个BFS的时候每个元素按序入栈

### 代码

```Python3 []
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        In = [0] * numCourses
        connect = defaultdict(set)
        for a, b in prerequisites:
            connect[b].add(a)
            In[a] += 1
        q = deque([])
        for i in range(numCourses):
            if not In[i]:
                q.append(i)
        ans = []
        while q:
            i = q.popleft()
            ans.append(i)
            for j in connect[i]:
                In[j] -= 1
                if not In[j]:
                    q.append(j)
        return ans if len(ans) == numCourses else []
```
```Java []
class Solution {
    int[] in, ans;
    Map<Integer, List<Integer>> map;
    Deque<Integer> q;
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        in = new int[numCourses];
        map = new HashMap<>();
        for(int i=0;i<prerequisites.length;i++){
            int a = prerequisites[i][0], b = prerequisites[i][1];
            in[a]++;
            List<Integer> cur = map.getOrDefault(b, new ArrayList<>());
            cur.add(a);
            map.put(b, cur);
        }
        q = new LinkedList<>();
        for(int i=0;i<numCourses;i++)
            if(in[i]==0)
                q.add(i);
        ans = new int[numCourses];
        int idx = 0;
        while(q.size() > 0){
            int i = q.pollFirst();
            ans[idx++] = i;
            if(map.containsKey(i))
                for(int j:map.get(i)){
                    in[j]--;
                    if(in[j]==0)
                        q.add(j);
                }
        }
        if(idx==numCourses)
            return ans;
        return new int[0];
    }
}
```