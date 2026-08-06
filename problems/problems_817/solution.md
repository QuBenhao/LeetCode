# [Python/Java/TypeScript/Go] 模拟

> slug: pythonjavatypescriptgo-mo-ni-by-himymben-9ir0
> date: 2022-10-11
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Linked List Components (linked-list-components)
> url: https://leetcode.cn/problems/linked-list-components/solutions/oqbFu1/pythonjavatypescriptgo-mo-ni-by-himymben-9ir0/

---
### 解题思路
使用哈希表记录所有数组中的数，在遍历链表时，判断当前数是否在哈希表中，计算答案和当前组件状态即可

### 代码

```Python3 []
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        node, vals, ans, cur = head, set(nums), 0, False
        while node:
            if not cur and node.val in vals:
                cur, ans = True, ans + 1
            elif cur and node.val not in vals:
                cur = False
            node = node.next
        return ans
```
```Java []
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int numComponents(ListNode head, int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num: nums) {
            set.add(num);
        }
        ListNode node = head;
        boolean cur = false;
        int ans = 0;
        while (node != null) {
            if (!cur && set.contains(node.val)) {
                ans++;
                cur = true;
            } else if (cur && !set.contains(node.val)) {
                cur = false;
            }
            node = node.next;
        }
        return ans;
    }
}
```
```TypeScript []
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

function numComponents(head: ListNode | null, nums: number[]): number {
    const set: Set<number> = new Set<number>(nums)
    let node: ListNode = head, ans: number = 0, cur: boolean = false
    while (node != null) {
        if (!cur && set.has(node.val)) {
            cur = true
            ans++
        } else if (cur && !set.has(node.val)) {
            cur = false
        }
        node = node.next
    }
    return ans
};
```
```Go []
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func numComponents(head *ListNode, nums []int) (ans int) {
    s, node, cur := map[int]bool{}, head, false
    for _, num := range nums {
        s[num] = true
    }
    for node != nil {
        if !cur && s[node.Val] {
            cur = true
            ans++
        } else if cur && !s[node.Val] {
            cur = false
        }
        node = node.Next
    }
    return
}
```