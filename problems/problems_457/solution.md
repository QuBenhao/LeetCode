# [Python/Java]  反着看这道题(无指针的空间o(1)?)

> Author: Benhao
> Date: 2021-08-07
> Upvotes: 10
> Tags: Java, Python, Python3

---

### 解题思路
构不成循环的点有什么情况呢？它的下一个点是它自己，或者它和下一个点的乘积小于等于0（相反的数或者0，相当于进了一个构不成循环的地方，所以可以改成0，不影响存在的循环）。
修改后，所有指向这些0的点，又都是新的构不成循环的点，以此类推。如果我们持续做这种变化，直到我们没有任何地方可以变化。最后如果数组中存在不为0的地方，那他们就是那个循环的地方。

### 代码
省空间费时间
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
                # Python里负数取模为正
                nxt = (i + num) % n
                # 指向自己、指向正负相反的地方、指向0,均构不成循环
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
费空间省时间
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