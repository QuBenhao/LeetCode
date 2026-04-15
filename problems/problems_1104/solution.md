# [Python/Java] 两种极其简单的递推公式(双百)

> Author: Benhao
> Date: 2021-07-28
> Upvotes: 4
> Tags: Java, Python, Python3

---

### 解题思路
我将每一层进入的端点称为入口端点，将要变成下一行的端点称为出口端点。
每一层的入口端点一定是$2^n$，出口端点一定是$2^{n+1}-1$.
**某一层的某个点到该层的入口端点的距离除以2**就是**上一层它的父亲节点到上一层出口端点的距离**
或者
**某一层的某个点到该层的出口端点的距离除以2**就是**上一层它的父亲节点到上一层入口端点的距离**

$x = 2^n + k, y = 2^n - 1 - k/2$，其中$x$为节点，$y$为其父亲节点

> 比如在第一个例子中，14到它的入口端点8的距离为6，那么它的父亲节点到它那层的出口端点的距离为3,也就是7-3=4。
而4到4的距离为0，所以下一个为3-0=3，以此类推。
其实本质上这是因为二叉树这样标号，每层节点个数总满足是上一层的两倍导致的。
当你计算自己到端点的距离时，上一层到同一侧的这边端点的距离其实就是一个2倍的缩放！


### 代码
向小的那一边缩放
```python3 []
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        # 初始入口端点
        last = 2 ** int(log(label, 2))
        while label > 1:
            # 上一层节点到其出口端点的距离
            add = label - last >> 1
            # 计算父亲节点的值 
            label = last - 1 - add
            # 下一个入口端点必然是除以2的关系
            last >>= 1
            ans.append(label)
        return ans[::-1]
```
```python3 []
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 求小于等于x的最接近x的2次幂，也就是入口的端点值
        def closest(x):
            if not x & (x-1):
                return x
            x -= 1
            x |= x>>1
            x |= x>>2
            x |= x>>4
            x |= x>>8
            x |= x>>16
            return x + 1 >> 1 if x >= 0 else 1

        ans = [label]
        # 初始入口端点
        last = closest(label)
        while label > 1:
            # 上一层节点到其出口端点的距离
            add = label - last >> 1
            # 计算父亲节点的值 
            label = last - 1 - add
            # 下一个入口端点必然是除以2的关系
            last >>= 1
            ans.append(label)
        return ans[::-1]

```
```java []
class Solution {
    public List<Integer> pathInZigZagTree(int label) {
        ArrayList<Integer> ans = new ArrayList<>();
        ans.add(label);
        int last = closest(label);
        while(label > 1){
            int add = label - last >> 1;
            label = last - 1 - add;
            last >>= 1;
            ans.add(label);
        }
        Collections.reverse(ans);
        return ans;
    }

    public int closest(int x){
        if((x & (x-1))==0)
            return x;
        x--;
        x |= x >>> 1;
        x |= x >>> 2;
        x |= x >>> 4;
        x |= x >>> 8;
        x |= x >>> 16;
        if (x >= 0)
            return x + 1 >> 1;
        return 1;
    }
}
```

向大的那一边缩放
```python3 []
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = [label]
        # 初始出口端点
        last = 2 ** (int(log(label, 2)) + 1)
        while label > 1:
            # 上一层节点到其入口端点的距离
            dis = last - 1 - label >> 1
            # 计算父亲节点的值 
            label = last//4 + dis
            # 下一个出口端点必然是除以2的关系
            last >>= 1
            ans.append(label)
        return ans[::-1]
```
```python3 []
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 求大于x的最接近x的2次幂，也就是出口的端点值
        def closest(x):
            if not x & (x-1):
                x += 1
            x -= 1
            x |= x>>1
            x |= x>>2
            x |= x>>4
            x |= x>>8
            x |= x>>16
            return x + 1 if x >= 0 else 1

        ans = [label]
        # 初始出口端点
        last = closest(label)
        while label > 1:
            # 上一层节点到其入口端点的距离
            dis = last - 1 - label >> 1
            # 计算父亲节点的值 
            label = last//4 + dis
            # 下一个出口端点必然是除以2的关系
            last >>= 1
            ans.append(label)
        return ans[::-1]
```
```java []
class Solution {
    public List<Integer> pathInZigZagTree(int label) {
        ArrayList<Integer> ans = new ArrayList<>();
        ans.add(label);
        int last = closest(label);
        while(label > 1){
            int dis = last - 1 - label >> 1;
            last >>= 1;
            label = (last/2) + dis;
            ans.add(label);
        }
        Collections.reverse(ans);
        return ans;
    }

    public int closest(int x){
        if((x & (x-1))==0)
            x++;
        x--;
        x |= x >>> 1;
        x |= x >>> 2;
        x |= x >>> 4;
        x |= x >>> 8;
        x |= x >>> 16;
        if (x >= 0)
            return x + 1;
        return 1;
    }
}
```
