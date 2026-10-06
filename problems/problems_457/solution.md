# [Python/Java] Think backward about this problem (o(1) space without pointers?)

> Author: Benhao
> Date: 2021-08-07
> Upvotes: 10
> Tags: Java, Python, Python3

---

### Approach
Which nodes cannot form a valid cycle? A node whose next node is itself, or whose value times the next value is at most 0. Opposite signs or a zero lead somewhere that cannot form a valid cycle, so mark the node as 0 without affecting any existing valid cycle.
After marking, every node pointing to these zeros is another node that cannot form a cycle. Repeat until no changes remain. Any nonzero values left in the array then belong to a cycle.

### Code
Save space at the cost of time
```Python3 []
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        change = True
        while change:
            change = False
            for i, num in enumerate(nums):
                if not num:
                    continue
                # In Python, modulo with a positive divisor gives a nonnegative result even for negative values
                nxt = (i + num) % n
                # A node pointing to itself, an opposite-sign value, or 0 cannot form a valid cycle
                if nxt == i or nums[nxt] * num <= 0:
                    change = True
                    nums[i] = 0
        return any(num for num in nums)
```
```Java []
class Solution {
    public boolean circularArrayLoop(int[] nums) {
        int n = nums.length;
        boolean change = true;
        while(change){
            change = false;
            for(int i=0;i<n;i++){
                if(nums[i] == 0)
                    continue;
                int nxt = ((i + nums[i]) % n + n) % n;
                if(nxt == i || nums[nxt] * nums[i] <= 0){
                    change = true;
                    nums[i] = 0;
                }
            }
        }
        for(int i=0;i<n;i++)
            if(nums[i]!=0)
                return true;
        return false;
    }
}
```
Save time at the cost of space
```Python3 []
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        connect = defaultdict(list)
        marks = deque([])
        for i, num in enumerate(nums):
            nxt = (i + num) % n
            connect[nxt].append(i)
            if nxt == i or nums[nxt] * num < 0:
                marks.append(i)
                nums[i] = 0
        while marks:
            i = marks.popleft()
            for nxt in connect[i]:
                if nums[nxt]:
                    nums[nxt] = 0
                    marks.append(nxt)
        return any(num for num in nums)
```
```Python3 []
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        connect = defaultdict(list)
        marks = deque([])
        ans = 0
        for i, num in enumerate(nums):
            nxt = (i + num) % n
            connect[nxt].append(i)
            if nxt == i or nums[nxt] * num < 0:
                marks.append(i)
                nums[i] = 0
        while marks:
            i = marks.popleft()
            ans += 1
            for nxt in connect[i]:
                if nums[nxt]:
                    marks.append(nxt)
                    nums[nxt] = 0
        return ans < n
```
```Java []
class Solution {
    int n, ans;
    Map<Integer, List<Integer>> connect;
    Deque<Integer> marks;
    public boolean circularArrayLoop(int[] nums) {
        n = nums.length;
        connect = new HashMap<>();
        marks = new LinkedList<>();
        ans = 0;
        for(int i=0;i<n;i++){
            int nxt = ((i+nums[i])%n+n)%n;
            List<Integer> cur = connect.getOrDefault(nxt, new ArrayList<>());
            cur.add(i);
            connect.put(nxt, cur);
            if(nxt == i || nums[nxt] * nums[i] <= 0){
                marks.add(i);
                nums[i] = 0;
            }
        }
        while(!marks.isEmpty()){
            int i = marks.pollFirst();
            ans++;
            if(connect.containsKey(i)){
                for(int nxt: connect.get(i)){
                    if(nums[nxt] != 0){
                        marks.add(nxt);
                        nums[nxt] = 0;
                    }
                }
            }
        }
        return ans < n;
    }
}
```
