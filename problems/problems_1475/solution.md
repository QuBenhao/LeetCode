# [Python/Java/TypeScript/Go] Monotonic stack

> slug: pythonjavatypescriptgo-dan-diao-zhan-by-0f3uz
> date: 2022-09-01
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Final Prices With a Special Discount in a Shop (final-prices-with-a-special-discount-in-a-shop)
> url: https://leetcode.cn/problems/final-prices-with-a-special-discount-in-a-shop/solutions/Y3HcHo/pythonjavatypescriptgo-dan-diao-zhan-by-0f3uz/

---
### Approach
We need the next element less than or equal to each element, which naturally suggests a monotonic stack.
Maintain a monotonically increasing stack of elements that have not yet found a later element less than or equal to themselves.
When a smaller element appears, keep popping the stack as appropriate: the current value is the first value less than or equal to each popped element.
Elements with no later value less than or equal to them keep their original values. Alternatively, append 0 to ensure that every element is popped.

### Code

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
