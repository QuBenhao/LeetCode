# [Python/Java/JavaScript/Go] Binary search

> slug: pythonjavajavascriptgo-er-fen-cha-zhao-b-bqfc
> date: 2021-12-10
> tags: Go, Java, JavaScript, Python, Python3
> question: Online Election (online-election)
> url: https://leetcode.cn/problems/online-election/solutions/VRETOa/pythonjavajavascriptgo-er-fen-cha-zhao-b-bqfc/

---
### Approach
Because queries are online, precompute the answer at every voting time during initialization.
For a later query between two voting times, use the answer at the earlier time, since it does not change in between;
For a query at an exact voting time, use that time's answer.

### Code

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
