# [Python/Java/TypeScript/Go] 单调栈

> slug: pythonjavatypescriptgo-dan-diao-zhan-by-0f3uz
> date: 2022-09-01
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Final Prices With a Special Discount in a Shop (final-prices-with-a-special-discount-in-a-shop)
> url: https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/solutions/Y3HcHo/pythonjavatypescriptgo-dan-diao-zhan-by-0f3uz/

---
### 解题思路
本题要找每个元素的下一个小于等于它的元素，很容易想到单调栈。
具体来说，我们维护一个单调递增栈，栈里面的元素都是没找到小于等于自己的元素的。
当出现一个比栈顶小的元素时，我们根据大小不停地弹出栈顶 (这个数就是小于等于该栈顶的第一个数了)。
最后将没有出现小于等于的元素赋予原值即可 (或者在末尾添加0保证所有人都弹出)

### 代码

```Python3 []
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack, ans = [], [-1] * len(prices)
        for i, p in enumerate(prices + [0]):
            while stack and stack[-1][0] >= p:
                price, idx = stack.pop()
                ans[idx] = price - p
            stack.append((p, i))
        return ans
```
```Python3 []
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack, ans = [], [-1] * len(prices)
        for i, p in enumerate(prices):
            while stack and stack[-1][0] >= p:
                price, idx = stack.pop()
                ans[idx] = price - p
            stack.append((p, i))
        for p, idx in stack:
            ans[idx] = p
        return ans
```
```Java []
class Solution {
    public int[] finalPrices(int[] prices) {
        int[] ans = new int[prices.length];
        Deque<Pair<Integer, Integer>> stack = new ArrayDeque<>();
        for (int i = 0; i <= prices.length; i++) {
            int price = i == prices.length ? 0 : prices[i];
            while (!stack.isEmpty() && stack.peekLast().getKey() >= price) {
                Pair<Integer, Integer> pair = stack.removeLast();
                ans[pair.getValue()] = pair.getKey() - price;
            }
            stack.addLast(new Pair<Integer, Integer>(price, i));
        }
        return ans;
    }
}
```
```TypeScript []
function finalPrices(prices: number[]): number[] {
    const ans: Array<number> = new Array<number>(prices.length).fill(0), stack: Array<Array<number>> = new Array<Array<number>>()
    for (let i = 0; i <= prices.length; i++) {
        const price = i === prices.length ? 0 : prices[i]
        while (stack.length > 0 && stack[stack.length - 1][0] >= price) {
            const [lastPrice, idx] = stack.pop()
            ans[idx] = lastPrice - price
        }
        stack.push([price, i])
    }
    return ans
};
```
```Go []
func finalPrices(prices []int) []int {
    n := len(prices)
    ans, stack := make([]int, n), [][]int{}
    for i, p := range append(prices, 0) {
        for len(stack) > 0 && stack[len(stack) - 1][0] >= p {
            cur := stack[len(stack) - 1]
            stack = stack[:len(stack) - 1]
            ans[cur[1]] = cur[0] - p
        }
        stack = append(stack, []int{p, i})
    }
    return ans
}
```