# [Python/Java/JavaScript] 并查集 

> slug: pythonjavajavascript-bing-cha-ji-by-himy-5elv
> date: 2021-10-08
> tags: Java, JavaScript, Python, Python3
> question: Data Stream as Disjoint Intervals (data-stream-as-disjoint-intervals)
> url: https://leetcode.cn/problems/data-stream-as-disjoint-intervals/solutions/esNxzC/pythonjavajavascript-bing-cha-ji-by-himy-5elv/

---
### 解题思路
[并查集讲解可以看](https://zhuanlan.zhihu.com/p/93647900/)

### 代码

```Python3 []
from sortedcontainers import SortedSet
class SummaryRanges:

    def __init__(self):
        self.find = [i for i in range(10002)]
        self.points = SortedSet()

    def addNum(self, val: int) -> None:
        self.points.add(val)
        self.find[val] = self.find[val + 1]

    def getIntervals(self) -> List[List[int]]:
        ans = []
        for p in self.points:
            if ans and p <= ans[-1][1]:
                continue
            ans.append([p, self.f(p) - 1])
        return ans
    
    def f(self, x):
        if x == self.find[x]:
            return x
        self.find[x] = self.f(self.find[x])
        return self.find[x]
```
```Java []
class SummaryRanges {
    int[] nums;
    public SummaryRanges() {
        nums = new int[10002];
    }
    
    public void addNum(int val) {
        if(nums[val] == 0)
            nums[val] = val + 1;
        find(val);
    }
    
    public int[][] getIntervals() {
        List<int[]> ans = new ArrayList<>();
        for(int i=0;i<10001;){
            if(nums[i] != 0){
                int tmp = find(nums[i]) - 1;
                ans.add(new int[]{i, tmp});
                i = tmp + 1;
            }
            else
                i++;
        }
        int[][] res = new int[ans.size()][2];
        int idx = 0;
        for(int[] data:ans){
            res[idx][0] = data[0];
            res[idx++][1] = data[1];
        }
        return res;
    }

    private int find(int x){
        if(nums[x] == 0)
            return x;
        nums[x] = find(nums[x]);
        return nums[x];
    }
}
```
```JavaScript []
let nums;
var SummaryRanges = function() {
    nums = new Array(10002);
};

/** 
 * @param {number} val
 * @return {void}
 */
SummaryRanges.prototype.addNum = function(val) {
    if(nums[val] === undefined)
        nums[val] = val + 1;
    finds(val);
};

/**
 * @return {number[][]}
 */
SummaryRanges.prototype.getIntervals = function() {
    let ans = new Array();
    for(let i=0;i<10001;){
        if(nums[i] != undefined){
            let tmp = new Array(2);
            tmp[0] = i;
            tmp[1] = finds(nums[i]) - 1;
            i = tmp[1] + 1;
            ans.push(tmp);
        }
        else
            i++;
    }
    return ans;
};

var finds = function(x) {
    if(nums[x] == undefined)
        return x;
    nums[x] = finds(nums[x]);
    return nums[x];
}
```