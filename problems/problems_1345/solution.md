# [Python/Java/JavaScript/Go] BFS

> Author: Benhao
> Date: 2022-01-20
> Upvotes: 18
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
只需要注意像公交车站那道题、或者LCP变化的迷宫，处理每个数字的跳跃仅发生一次，就和BFS模板没有区别。

### 代码

```Python3 []
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        idx_map, steps = defaultdict(list), [len(arr) - 1] * len(arr)
        for i, num in enumerate(arr):
            idx_map[num].append(i)
        queue = deque([0])
        steps[0] = 0
        while queue:
            idx = queue.popleft()
            if idx == len(arr) - 1:
                break
            nxt_step = steps[idx] + 1
            idx_map[arr[idx]] += [idx+1,idx-1] if idx else [idx+1]
            while idx_map[arr[idx]]:
                if steps[(other:=idx_map[arr[idx]].pop())] > nxt_step:
                    steps[other] = nxt_step
                    queue.append(other)
        return steps[-1]
```
```Java []
class Solution {
    public int minJumps(int[] arr) {
        Map<Integer, List<Integer>> idxMap = new HashMap<>();
        int[] steps = new int[arr.length];
        for(int i=0;i<arr.length;i++){
            List<Integer> list = idxMap.getOrDefault(arr[i], new ArrayList<>());
            list.add(i);
            idxMap.put(arr[i], list); 
            steps[i] = arr.length - 1;
        }
        Deque<Integer> queue = new ArrayDeque<>();
        queue.addLast(0);
        steps[0] = 0;
        while(!queue.isEmpty()){
            int idx = queue.pollFirst();
            if(idx == arr.length - 1)
                break;
            int nxtStep = steps[idx] + 1;
            List<Integer> list = idxMap.getOrDefault(arr[idx], new ArrayList<>());
            list.add(idx + 1);
            if(idx > 0)
                list.add(idx - 1);
            for(int other: list)
                if(steps[other] > nxtStep){
                    steps[other] = nxtStep;
                    queue.addLast(other);
                }
            idxMap.remove(arr[idx]);
        }
        return steps[arr.length - 1];
    }
}
```
```JavaScript []
/**
 * @param {number[]} arr
 * @return {number}
 */
var minJumps = function(arr) {
    const idxMap = new Map(), explored = new Set()
    for(let i=0;i<arr.length;i++){
        if(idxMap.has(arr[i]))
            idxMap.get(arr[i]).push(i)
        else
            idxMap.set(arr[i], [i])
    }
    let nodes = [0], step = 0
    explored.add(0)
    while(nodes.length > 0){
        const nxt = new Array()
        for(const cur of nodes){
            if(cur == arr.length - 1)
                return step
            if(idxMap.has(arr[cur])){
                for(const other of idxMap.get(arr[cur])){
                    if(!explored.has(other)){
                        explored.add(other)
                        nxt.push(other)
                    }
                }
                idxMap.delete(arr[cur])
            }
            if(!explored.has(cur + 1)){
                explored.add(cur + 1)
                nxt.push(cur + 1)               
            }
            if(cur > 0 && !explored.has(cur - 1)){
                explored.add(cur - 1)
                nxt.push(cur - 1)
            }
        }
        nodes = nxt
        step++
    }
    return arr.length - 1
};
```
```Golang []
func minJumps(arr []int) int {
    idxMap, steps := map[int][]int{}, make([]int, len(arr))
    for i := 0; i < len(arr); i++ {
        l := idxMap[arr[i]]
        l = append(l, i)
        idxMap[arr[i]] = l
        steps[i] = len(arr) - 1
    }
    queue := []int{0}
    steps[0] = 0
    for len(queue) > 0 {
        idx := queue[0]
        if idx == len(arr) - 1{
            break
        }
        nxtStep := steps[idx] + 1
        queue = queue[1:]
        l, ok := idxMap[arr[idx]]
        if ok {
            for _, other := range l {
                if steps[other] > nxtStep {
                    steps[other] = nxtStep
                    queue = append(queue, other)
                }
            }
            delete(idxMap, arr[idx])
        }
        if other := idx + 1; steps[other] > nxtStep {
            steps[other] = nxtStep
            queue = append(queue, other)
        }
        if idx > 0{
            if other := idx - 1; steps[other] > nxtStep {
                steps[other] = nxtStep
                queue = append(queue, other)
            }
        }
    }
    return steps[len(arr) - 1]
}
```