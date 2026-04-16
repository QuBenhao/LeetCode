# [Python/Java] 最长上升子序列

> Author: Benhao
> Date: 2021-07-26
> Upvotes: 29
> Tags: Java, Python, Python3

---

### 解题思路
本题要找最少操作次数，实际上就是找最长的公共子序列(这样需要的操作最少);
根据target中互不相同，我们知道每个数字对应的坐标唯一;
于是最长公共子序列等价于arr用target的坐标转换后构成最长的上升子序列.

这是因为:
**不管怎么样，公共子序列在target中必然是从左到右的，那么他们的坐标自然是从小到大的**

### 代码
```python3 []
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        # 分析:
        # 本题要找最少操作次数，实际上就是找最长的公共子序列(这样需要的操作最少)
        # 根据target中互不相同，我们知道每个数字对应的坐标唯一
        # 于是最长公共子序列等价于arr用target的坐标转换后构成最长的上升子序列

        # 数字对应坐标
        idx_dict = {num: i for i, num in enumerate(target)}
        # 300.最长上升子序列
        stack = []
        for num in arr:
            # 只有在target的数字才可能属于公共子序列
            if num in idx_dict:
                # 转换坐标
                idx = idx_dict[num]
                # 该坐标在当前栈中的位置
                i = bisect.bisect_left(stack, idx)
                # 如果在最后要加入元素，否则要修改该位置的元素
                # 跟一般的讲，i代表了目前这个idx在stack中的大小位置，
                # 在前面出现还比idx大的stack中的元素是无法和idx构成最长上升子序列的。
                # i左边的数比idx小，可以和idx构成上升子序列，(idx构成的长度就是i+1)
                # idx比i的值小，将i替换后可以方便后面构成更优的子序列(越小后面能加入的数越多)
                if i == len(stack):
                    stack.append(0)
                stack[i] = idx
        # 最终stack的长度就构成了最长上升子序列的长度，用减法即可得到本题答案
        return len(target) - len(stack)
```
```java []
class Solution {
    public int minOperations(int[] target, int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i=0;i<target.length;i++)
            map.put(target[i], i);
        ArrayList<Integer> stack = new ArrayList<>();
        for(int num:arr){
            Integer idx = map.get(num);
            if(idx != null){
                int l=0,r=stack.size();
                while(l<r){
                    int mid = l + r >> 1;
                    if(stack.get(mid) >= idx)
                        r = mid;
                    else
                        l = mid + 1;
                }
                if(l == stack.size())
                    stack.add(idx);
                else
                    stack.set(l, idx);
            }
        } 
        return target.length - stack.size();
    }
}
```
