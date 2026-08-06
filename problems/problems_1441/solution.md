# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavatypescriptgo-mo-ni-by-himymben-xheb
> date: 2022-10-14
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Build an Array With Stack Operations (build-an-array-with-stack-operations)
> url: https://leetcode.cn/problems/build-an-array-with-stack-operations/solutions/QnlPDU/pythonjavatypescriptgo-mo-ni-by-himymben-xheb/

---
### 解题思路
每一个缺失的数字就填入一组"Push"和"Pop"即可

### 代码

```Python3 []
class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans, diff = [], 0
        for i, v in enumerate(target, 1):
            if i + diff == v:
                ans.append("Push")
            else:
                ans += ["Push", "Pop"] * (v - i - diff)
                ans.append("Push")
                diff = v - i
        return ans
```
```Java []
class Solution {
    public List<String> buildArray(int[] target, int n) {
        List<String> ans = new ArrayList<>();
        for (int i = 0, j = 1; i < target.length; i++, j++) {
            for (; j < target[i]; j++) {
                ans.add("Push");
                ans.add("Pop");
            }
            ans.add("Push");
        }
        return ans;
    }
}
```
```TypeScript []
function buildArray(target: number[], n: number): string[] {
    const ans: Array<string> = new Array<string>()
    for (let i = 0, j = 1; i < target.length; i++, j++) {
        for (; j < target[i]; j++) {
            ans.push("Push")
            ans.push("Pop")
        }
        ans.push("Push")
    }
    return ans
};
```
```Go []
func buildArray(target []int, n int) (ans []string) {
    for i, j := 0, 1; i < len(target); i++ {
        for ; j < target[i]; j++ {
            ans = append(ans, "Push")
            ans = append(ans, "Pop")
        }
        ans = append(ans, "Push")
        j++
    }
    return
}
```