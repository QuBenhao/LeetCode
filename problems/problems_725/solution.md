# [Python/Java] 模拟

> slug: pythonjava-mo-ni-by-himymben-eovi
> date: 2021-09-21
> tags: Java, Python, Python3
> question: Split Linked List in Parts (split-linked-list-in-parts)
> url: https://leetcode.cn/problems/split-linked-list-in-parts/solutions/jTGKVT/pythonjava-mo-ni-by-himymben-eovi/

---
### 解题思路
先统计链表的长度，然后根据链表的长度和k判断每段的长度(除数和余数)，除数是每个的基础长度，而余数是前多少个需要额外多一个。

### 代码

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