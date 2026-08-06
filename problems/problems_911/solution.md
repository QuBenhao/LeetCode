# [Python/Java/JavaScript/Go] 二分查找

> slug: pythonjavajavascriptgo-er-fen-cha-zhao-b-bqfc
> date: 2021-12-10
> tags: Go, Java, JavaScript, Python, Python3
> question: Online Election (online-election)
> url: https://leetcode.cn/problems/online-election/solutions/VRETOa/pythonjavajavascriptgo-er-fen-cha-zhao-b-bqfc/

---
### 解题思路
因为本题为在线查询，所以需要在初始化的时候统计所有投票时刻的答案。
这样后面查询在时刻之间的时刻，答案肯定是上一个时刻的答案（因为这期间不会变了）；
在查询某一时刻的答案，答案就是该时刻的答案。

### 代码

```Python3 []
class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        n = len(times)
        cnts, cur = defaultdict(int), None
        self.ans, self.times = [-1] * n, times
        for i in range(n):
            cnts[persons[i]] += 1
            if cur is None or cnts[persons[i]] >= cnts[cur]:
                cur = persons[i]
            self.ans[i] = cur

    def q(self, t: int) -> int:
        return self.ans[bisect_right(self.times, t) - 1]



# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
```
```Java []
class TopVotedCandidate {
    private int[] times;
    private int[] ans;
    public TopVotedCandidate(int[] persons, int[] times) {
        this.times = times;
        ans = new int[times.length];
        int[] cnts = new int[times.length];
        int cur = -1;
        for(int i=0;i<times.length;i++){
            cnts[persons[i]]++;
            if(cur == -1 || cnts[persons[i]] >= cnts[cur])
                cur = persons[i];
            ans[i] = cur;
        }
    }
    
    public int q(int t) {
        int l = 0, r = times.length;
        while(l<r){
            int mid = l + (r - l) / 2;
            if(times[mid] <= t)
                l = mid + 1;
            else
                r = mid;
        }
        return ans[l-1];
    }
}

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * TopVotedCandidate obj = new TopVotedCandidate(persons, times);
 * int param_1 = obj.q(t);
 */
```
```JavaScript []
/**
 * @param {number[]} persons
 * @param {number[]} times
 */
var TopVotedCandidate = function(persons, times) {
    const n = times.length
    this.ans = new Array(n)
    this.times = times
    const cnts = new Array(n)
    cnts.fill(0)
    for(let i=0,cur=-1;i<n;i++){
        cnts[persons[i]]++
        if(cur == -1 || cnts[persons[i]] >= cnts[cur])
            cur = persons[i]
        this.ans[i] = cur
    }
};

/** 
 * @param {number} t
 * @return {number}
 */
TopVotedCandidate.prototype.q = function(t) {
    let l = 0, r = this.times.length
    while(l < r){
        const mid = l + Math.floor((r - l) / 2)
        if(this.times[mid] <= t)
            l = mid + 1
        else
            r = mid
    }
    return this.ans[l - 1]
};

/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * var obj = new TopVotedCandidate(persons, times)
 * var param_1 = obj.q(t)
 */
```
```Go []
type TopVotedCandidate struct {
    ans, times []int
}


func Constructor(persons []int, times []int) TopVotedCandidate {
    n := len(times)
    ans, cnts, cur := make([]int, n), make([]int, n), -1
    for i := range times {
        cnts[persons[i]]++
        if cur == -1 || cnts[persons[i]] >= cnts[cur] {
            cur = persons[i]
        }
        ans[i] = cur
    }
    return TopVotedCandidate{ans, times}
}


func (this *TopVotedCandidate) Q(t int) int {
    l, r := 0, len(this.times)
    for l < r {
        mid := l + (r - l)/2
        if this.times[mid] <= t {
            l = mid + 1
        } else {
            r = mid
        }
    }
    return this.ans[l - 1]
}


/**
 * Your TopVotedCandidate object will be instantiated and called as such:
 * obj := Constructor(persons, times);
 * param_1 := obj.Q(t);
 */
```