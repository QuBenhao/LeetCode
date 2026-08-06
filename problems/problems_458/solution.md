# [Python/Java/JavaScript/Go] 很经典的一道进制转换思维模式题

> slug: pythonjavajavascriptgo-hen-jing-dian-de-qilwu
> date: 2021-11-24
> tags: Go, Java, JavaScript, Python, Python3
> question: Poor Pigs (poor-pigs)
> url: https://leetcode.cn/problems/poor-pigs/solutions/G8HAk4/pythonjavajavascriptgo-hen-jing-dian-de-qilwu/

---
### 解题思路
```python3
# 特别经典的一道题，1024个桶里，有一个有毒，十个小白鼠可以做测试，怎么一次找到有毒的那个
# 将0~1023写成二进制，最多是十位，每个小白鼠喝所有某一位为1的（一鼠一位）
# 最终要找的那个就是所有死的小白鼠的位为1，其他位为0
# 我们知道十只小白鼠一次可以试出2^10个桶，如果是两次呢？
# 其实两次可以看成三进制，每个小白鼠可以在两轮内试出某一位是0还是1还是2
# 第一次死就是那一位为1，第二次是那一次为2，没死就是那一位为0
# 这样来看的话，
# x轮就该转换成(x+1)进制, 我们要找buckets在x+1进制下是几位，就是我们至少需要的小白鼠个数了
```

感谢各位一直以来的陪伴和鼓励！一起继续加油啊！感恩节快乐～

[关于这样信息熵最大化的解释可以看三叶的题解](https://leetcode.cn/problems/poor-pigs/solution/gong-shui-san-xie-jin-zhi-cai-xiang-xian-69fl/)

### 代码

```python3 []
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets, minutesToTest//minutesToDie + 1))
```
```Java []
class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        // 这里用了一个换底公式
        return (int)Math.ceil(Math.log(buckets)/Math.log(minutesToTest/minutesToDie + 1));
    }
}
```
```JavaScript []
/**
 * @param {number} buckets
 * @param {number} minutesToDie
 * @param {number} minutesToTest
 * @return {number}
 */
var poorPigs = function(buckets, minutesToDie, minutesToTest) {
    return Math.ceil(Math.log(buckets)/Math.log(Math.floor(minutesToTest/minutesToDie) + 1))
};
```
```Go []
func poorPigs(buckets int, minutesToDie int, minutesToTest int) int {
    return int(math.Ceil(math.Log(float64(buckets)) / math.Log(float64(minutesToTest/minutesToDie) + 1)))
}
```