# [Python/Java] 拓扑排序

> Author: Benhao
> Date: 2021-08-05
> Upvotes: 1
> Tags: Java, Python, Python3

---

### 解题思路
需要前置课程的课程在其前置课修完前是不可以修的，所以我们统计所有入度，修完所有入度为0的课程并减去他们的边直到所有能修的都修了。

### 代码

```Python3 []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 我们只能从没有prerequire的课程开始
        In = [0] * numCourses
        connect = defaultdict(list)
        for a, b in prerequisites:
            connect[b].append(a)
            In[a] += 1
        q = deque([])
        for i in range(numCourses):
            if not In[i]:
                q.append(i)
        while q:
            i = q.popleft()
            for j in connect[i]:
                In[j] -= 1
                if not In[j]:
                    q.append(j)
        return all(not In[i] for i in range(numCourses))
```
```Java []
class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] in = new int[numCourses];
        Map<Integer, List<Integer>> connect = new HashMap<>();
        for(int i=0;i< prerequisites.length;i++){
            int a = prerequisites[i][0], b = prerequisites[i][1];
            in[a]++;
            List<Integer> cur = connect.getOrDefault(b, new ArrayList<>());
            cur.add(a);
            connect.put(b, cur);
        }
        Deque<Integer> q = new LinkedList<>();
        for(int i=0;i<numCourses;i++)
            if(in[i]==0)
                q.add(i);
        while(q.size() > 0){
            int i = q.pollFirst();
            if(connect.containsKey(i))
                for(int j:connect.get(i)){
                    in[j]--;
                    if(in[j] == 0)
                        q.add(j);
                }
        }
        for(int i=0;i<numCourses;i++)
            if(in[i] > 0)
                return false;
        return true;
    }
}
```