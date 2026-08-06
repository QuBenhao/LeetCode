# [Python/Java/JavaScript] 模拟

> slug: pythonjavajavascript-mo-ni-by-himymben-d652
> date: 2021-10-12
> tags: Java, JavaScript, Python, Python3
> question: Fizz Buzz (fizz-buzz)
> url: https://leetcode.cn/problems/fizz-buzz/solutions/5BCr3b/pythonjavajavascript-mo-ni-by-himymben-d652/

---
```Python3 []
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n + 1):
            if i % 3 and i % 5:
                ans.append(str(i))
            elif not i % 3 and not i % 5:
                ans.append("FizzBuzz")
            elif not i % 3:
                ans.append("Fizz")
            else:
                ans.append("Buzz")
        return ans
```
```Java []
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> ans = new ArrayList<>();
        for(int i=1;i<=n;i++){
            if(i % 3 != 0 && i % 5 != 0)
                ans.add("" + i);
            else if(i%3 == 0 && i % 5 == 0)
                ans.add("FizzBuzz");
            else if(i%3 == 0)
                ans.add("Fizz");
            else
                ans.add("Buzz");
        }
        return ans;
    }
}
```
```JavaScript []
/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    // 今天是把Java代码复制粘贴过来的一天
    const ans = [];
    for(let i=1;i<=n;i++){
        if(i % 3 != 0 && i % 5 != 0)
            ans.push("" + i);
        else if(i%3 == 0 && i % 5 == 0)
            ans.push("FizzBuzz");
        else if(i%3 == 0)
            ans.push("Fizz");
        else
            ans.push("Buzz");
    }
    return ans;
};
```