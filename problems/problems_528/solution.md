# [Python] 前缀和+随机数二分查找

> Author: Benhao
> Date: 2021-08-29
> Upvotes: 19
> Tags: Java, Python, Python3

---

### 解题思路
题目可能比较难理解。直白的说就是你有一个空间很大的数组，然后对于每个坐标i，你有w[i]个i在这个数组中，最后随机从数组里选一个。
这么理解可以写出类似这样的代码，但是很费空间(我们先随机取10000个)。
```python3
class Solution:

    def __init__(self, w: List[int]):
        total = sum(w)
        self.list = [i for i in range(len(w))]
        self.weight = [0] * len(w)
        for i,num in enumerate(w):
            self.weight[i] += float(num/total)
        self.picks = random.choices(self.list, self.weight, k=10000)
        self.idx = -1

    def pickIndex(self) -> int:
        self.idx += 1
        return self.picks[self.idx]
```
那有什么办法可以更好的生成呢？

注意到如果第一个坐标有$k_0$个，那么它占用区间$[1,k_0]$，而第二个坐标有$k_1$个占用区间$[k_0+1,k_0+k_1]$，这个时候我们生成一个随机数在区间$[1,k_0+k_1]$，落在第一个坐标的区间概率为$\frac{k_0}{k_0+k_1}$，这是完全符合我们想要的。
而且，这个随机数可以根据二分查找对应回原来的坐标。相当于小于等于$k_0$对应坐标0，大于$k_0$小于$k_1$对应坐标1,依次类推。这样我们生成一个随机数即可。

### 代码

```Python3 []
class Solution:

    def __init__(self, w: List[int]):
        # 计算前缀和，这样可以生成一个随机数，根据数的大小对应分布的坐标
        self.presum = list(accumulate(w))

    def pickIndex(self) -> int:
        rand = random.randint(1, self.presum[-1])
        return bisect_left(self.presum, rand)
```
```Java []
class Solution {
    Random r = new Random();
    int n;
    int[] presum;
    public Solution(int[] w) {
        n = w.length;
        presum = w;
        for(int i=1;i<n;i++)
            presum[i] += presum[i-1];
    }
    
    public int pickIndex() {
        int rand = r.nextInt(presum[n-1]) + 1;
        return binarySearch(rand);
    }

    public int binarySearch(int x){
        int left = 0, right = n - 1;
        while(left < right){
            int mid = (left + right)/2;
            if(presum[mid] >= x)
                right = mid;
            else
                left = mid + 1;
        }
        return left;
    }
}
```