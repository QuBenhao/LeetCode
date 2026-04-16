# [Python/Java/TypeScript/Go] 区间DP

> Author: Benhao
> Date: 2022-06-30
> Upvotes: 16
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
讨论所有符号位置，每次找一个符号认为它是最后做运算，那么这个时候就需要递归得到两遍的结果。
由于有大量重复计算，按区间位置进行记忆化即可（dp）

### 代码

```Python3 []
OP_MAP = {"+": operator.add, "-": operator.sub, "*": operator.mul}
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        @lru_cache(None)
        def dfs(left: int, right: int) -> List[int]:
            if left == right:
                return [int(sp[left])]
            res = []
            # 找区间里的符号, 按符号分割左右（我们认为最后计算这个符号）
            for i in range(left + 1, right, 2):
                for left_set in dfs(left, i - 1):
                    for right_set in dfs(i + 1, right):
                        res.append(OP_MAP[sp[i]](left_set, right_set))
            return res

        sp = re.split(r"(\D)", expression)
        return list(dfs(0, len(sp) - 1))
```
```Java []
class Solution {
    private List<String> arr;
    public List<Integer> diffWaysToCompute(String expression) {
        arr = new ArrayList<>();
        int cur = 0, count = 1;
        for (int i = 0; i < expression.length(); i++) {
            if (expression.charAt(i) <= '9' && expression.charAt(i) >= '0') {
                cur = 10 * cur + (expression.charAt(i) - '0');
            } else {
                arr.add(String.valueOf(cur));
                arr.add(expression.substring(i, i + 1));
                cur = 0;
                count++;
            }
        }
        arr.add(String.valueOf(cur));
        List<Integer>[][] dp = new List[count][count];
        for (int i = 0; i < count; i++) {
            for (int j = 0; j < count; j++) {
                dp[i][j] = new ArrayList<>();
            }
        }
        return dfs(dp, 0, arr.size() - 1);
    }

    private List<Integer> dfs(List<Integer>[][] dp, int left, int right) {
        if (dp[left/2][right/2].isEmpty()) {
            if (left == right) {
                dp[left/2][right/2].add(Integer.parseInt(arr.get(left)));
            } else {
                for (int i = left + 1; i <= right - 1; i += 2) {
                    for (int leftRes: dfs(dp, left, i - 1)) {
                        for (int rightRes: dfs(dp, i + 1, right)) {
                            dp[left/2][right/2].add(calculate(leftRes, rightRes, arr.get(i)));
                        }
                    }
                }
            }
        }
        return dp[left/2][right/2];
    }

    private int calculate(int a, int b, String op) {
        int ans;
        switch(op) {
            case "+":
                ans = a + b;
                break;
            case "-":
                ans = a - b;
                break;
            case "*":
                ans = a * b;
                break;
            default:
                ans = 0;
        }
        return ans;
    }
}
```
```TypeScript []
function diffWaysToCompute(expression: string): number[] {
    const arr = new Array()
    let cur = 0, count = 1
    for (let i = 0; i < expression.length; i++) {
        if (expression.charCodeAt(i) >= '0'.charCodeAt(0) && expression.charCodeAt(i) <= '9'.charCodeAt(0)) {
            cur = cur * 10 + (expression.charCodeAt(i) - '0'.charCodeAt(0))
        } else {
            arr.push(cur)
            arr.push(expression.charAt(i))
            cur = 0
            count++
        }
    }
    arr.push(cur)
    const dp = new Array(count).fill(0).map(() => new Array(count).fill(0).map(() => new Array<number>()))
    const cal = function(left: number, right: number, op: string): number {
        let ans = 0
        switch (op) {
            case "+":
                ans = left + right
                break
            case "-":
                ans = left - right
                break
            case "*":
                ans = left * right
                break
            default:
        }
        return ans
    }
    const dfs = function(left: number, right: number): number[] {
        const leftIdx = left >> 1, rightIdx = right >> 1
        if (dp[leftIdx][rightIdx].length == 0) {
            if (left == right) {
                dp[leftIdx][rightIdx].push(arr[left])
            } else {
                for (let i = left + 1; i <= right - 1; i += 2) {
                    for (const leftRes of dfs(left, i - 1)) {
                        for (const rightRes of dfs(i + 1, right)) {
                            dp[leftIdx][rightIdx].push(cal(leftRes, rightRes, arr[i]))
                        }
                    }
                }
            }
        }
        return dp[leftIdx][rightIdx]
    }
    return dfs(0, arr.length - 1)
};
```
```Go []
func diffWaysToCompute(expression string) []int {
    nums, ops := []int{}, []rune{}
    cur := 0
    for _, ex := range expression {
        if ex >= '0' && ex <= '9' {
            cur = 10 * cur + (int)(ex - '0')
        } else {
            nums = append(nums, cur)
            ops = append(ops, ex)
            cur = 0
        }
    }
    nums = append(nums, cur)
    dp := make([][][]int, len(nums))
    for i := range dp {
        dp[i] = make([][]int, len(nums))
    }
    var dfs func(left, right int) []int
    dfs = func(left, right int) []int {
        lIdx, rIdx := left >> 1, right >> 1
        if len(dp[lIdx][rIdx]) == 0 {
            if left == right {
                dp[lIdx][rIdx] = append(dp[lIdx][rIdx], nums[lIdx])
            } else {
                for i := left + 1; i <= right - 1; i += 2 {
                    for _, leftRes := range dfs(left, i - 1) {
                        for _, rightRes := range dfs(i + 1, right) {
                            dp[lIdx][rIdx] = append(dp[lIdx][rIdx], cal(leftRes, rightRes, ops[i >> 1]))
                        }
                    }
                }
            }
        }
        return dp[lIdx][rIdx]
    }
    return dfs(0, len(nums) + len(ops) - 1)
}

func cal(left, right int, op rune) int {
    if op == '+' {
        return left + right
    } else if op == '-' {
        return left - right
    } else {
        return left * right
    }
}

```