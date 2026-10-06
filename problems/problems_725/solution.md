# [Python/Java] Simulation

> slug: pythonjava-mo-ni-by-himymben-eovi
> date: 2021-09-21
> tags: Java, Python, Python3
> question: Split Linked List in Parts (split-linked-list-in-parts)
> url: https://leetcode.cn/problems/split-linked-list-in-parts/solutions/jTGKVT/pythonjava-mo-ni-by-himymben-eovi/

---
### Approach
First count the list's length. Dividing it by k gives the base length of each part; the remainder tells how many leading parts need one extra node.

### Code

```Python3 []
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        cur, l = head, 0
        while cur:
            l += 1
            cur = cur.next
        each, remain = l // k, l % k
        cur, ans, idx = head, [None] * k, 0
        while cur:
            ans[idx] = cur
            last = None
            for i in range(each + (idx < remain)):
                last = cur
                cur = cur.next
            idx += 1
            last.next = None
        return ans
```
```Java []
class Solution {
    public ListNode[] splitListToParts(ListNode head, int k) {
        int len = 0;
        ListNode cur = head, last = null;
        while(cur != null){
            cur = cur.next;
            len++;
        }
        int each = len / k, remain = len % k, idx = 0;
        cur = head;
        ListNode[] ans = new ListNode[k];
        Arrays.fill(ans, null);
        while(cur != null){
            ans[idx++] = cur;
            for(int i=0;i<(idx <= remain? each + 1 : each);i++){
                last = cur;
                cur = cur.next;
            }
            last.next = null;
        }
        return ans;
    }
}
```
