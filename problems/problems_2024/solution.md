# [Python/Java/JavaScript/Go] Sliding window with two pointers

> Author: Benhao
> Date: 2022-03-28
> Upvotes: 21
> Tags: Go, Java, JavaScript, Python, Python3

---

### Approach
Find the longest interval in which the number of T characters is at most k or the number of F characters is at most k.
Use two pointers to maintain the leftmost valid interval ending at the current position, tracking the counts of T and F between the pointers.
Add the current T or F to its count. If the interval becomes invalid, remove the character at the left pointer from its count and advance that pointer until the interval is valid again.
For each right pointer, the leftmost valid left pointer gives the maximum interval length ending there.

### Code

```Python3 []
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        ans = left = cnts_t = cnts_f = 0
        for right, c in enumerate(answerKey):
            cnts_t += c == 'T'
            cnts_f += c == 'F'
            # The counts of t and f in the window cannot both exceed k; only k changes are allowed
            while cnts_t > k and cnts_f > k:
                # The change limit is exceeded, so move the window's left boundary to the right
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
