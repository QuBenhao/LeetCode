# [Python/Java/JavaScript] 最接近开根的因子

> slug: pythonjavajavascript-zui-jie-jin-kai-gen-yhge
> date: 2021-10-23
> tags: Java, JavaScript, Python, Python3
> question: Construct the Rectangle (construct-the-rectangle)
> url: https://leetcode.cn/problems/construct-the-rectangle/solutions/AiaEqp/pythonjavajavascript-zui-jie-jin-kai-gen-yhge/

---
```Python3 []
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for i in range(int(sqrt(area)), 0, -1):
            if not area % i:
                return [area//i, i]
```
```Java []
class Solution {
    public int[] constructRectangle(int area) {
        for(int i=(int)Math.sqrt(area);;i--)
            if(area % i == 0)
                return new int[]{area/i,i};
    }
}
```
```JavaScript []
/**
 * @param {number} area
 * @return {number[]}
 */
var constructRectangle = function(area) {
    for(let i=Math.floor(Math.sqrt(area));;i--)
        if(area % i == 0)
            return [area/i,i];
};
```