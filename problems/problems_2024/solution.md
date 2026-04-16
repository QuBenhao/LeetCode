# [Python/Java/JavaScript/Go] 双指针滑动窗口 

> Author: Benhao
> Date: 2022-03-28
> Upvotes: 21
> Tags: Go, Java, JavaScript, Python, Python3

---

### 解题思路
题目要求统计最长的区间，这个区间内 T的数目小于等于k 或 F的数目小于等于k。
我们使用双指针维护当前指针对应的最左区间，并维护两个指针间T和F的各自的数目。
加入当前指针的T或F的数目，如果导致当前区间的数目不满足题目要求，抛去左指针T或F的数目并移动左指针直到满足为止。
统计每个指针最左的指针，就是该指针对应的最大区间长度。

### 代码

```Python3 []
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = left = cnts_t = cnts_f = 0
        for right, c in enumerate(answerKey):
            cnts_t += c == 'T'
            cnts_f += c == 'F'
            # 当前区间内的t和f的个数不能都大于k，我们只能变k次
            while cnts_t > k and cnts_f > k:
                # 超过最大变动次数了，当前指针的区间最左要向右移动
                cnts_t -= answerKey[left] == 'T'
                cnts_f -= answerKey[left] == 'F'
                left += 1
            ans = max(ans, right - left + 1)
        return ans
```
```Java []
class Solution {
    public int maxConsecutiveAnswers(String answerKey, int k) {
        int ans = 0;
        for(int left = 0, right = 0, cntsT = 0, cntsF = 0; right < answerKey.length(); right++) {
            cntsT += answerKey.charAt(right) == 'T' ? 1 : 0;
            cntsF += answerKey.charAt(right) == 'F' ? 1 : 0;
            while(cntsT > k && cntsF > k) {
                cntsT -= answerKey.charAt(left) == 'T' ? 1 : 0;
                cntsF -= answerKey.charAt(left) == 'F' ? 1 : 0;
                left++;
            }
            ans = Math.max(ans, right - left + 1);
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {string} answerKey
 * @param {number} k
 * @return {number}
 */
const T = 'T'.charCodeAt(0), F = 'F'.charCodeAt(0)
var maxConsecutiveAnswers = function(answerKey, k) {
    let ans = 0
    for(let left = 0, right = 0, cntsT = 0, cntsF = 0; right < answerKey.length; right++) {
        cntsT += answerKey.charCodeAt(right) === T ? 1 : 0
        cntsF += answerKey.charCodeAt(right) === F ? 1 : 0
        while(cntsT > k && cntsF > k) {
            cntsT -= answerKey.charCodeAt(left) === T ? 1 : 0
            cntsF -= answerKey.charCodeAt(left) === F ? 1 : 0
            left++
        }
        ans = Math.max(ans, right - left + 1)
    }
    return ans
};
```
```Go []
func maxConsecutiveAnswers(answerKey string, k int) (ans int) {
    for left, right, cntsT, cntsF := 0, 0, 0, 0; right < len(answerKey); right++ {
        cntsT += cmp(answerKey[right], 'T')
        cntsF += cmp(answerKey[right], 'F')
        for cntsT > k && cntsF > k {
            cntsT -= cmp(answerKey[left], 'T')
            cntsF -= cmp(answerKey[left], 'F')
            left++
        }
        if length := right - left + 1; length > ans {
            ans = length
        }
    }
    return
}

func cmp(a, b byte) int {
    if a == b {
        return 1
    }
    return 0
}
```