# [Python/Java/JavaScript/Go/C] 费空间省时间偷个懒

> Author: Benhao
> Date: 2022-01-16
> Upvotes: 12
> Tags: C, Go, Java, JavaScript, Python, Python3, Golang

---

### 解题思路
蓄水池抽样还是很好的思路，只是每次都要随机整个链表长度的次数所以代价略大。不知道的家人们建议和[叶总](https://leetcode.cn/problems/linked-list-random-node/solution/gong-shui-san-xie-xu-shui-chi-chou-yang-1lp9d/)学一下。

### 代码

```Python3 []
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.nodes = head._list_node_to_array()

    def getRandom(self) -> int:
        return choice(self.nodes)
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
    List<Integer> nodes = new ArrayList<>();
    Random random = new Random(20220116);

    public Solution(ListNode head) {
        for(;head!=null;head=head.next)
            nodes.add(head.val);
    }
    
    public int getRandom() {
        return nodes.get(random.nextInt(nodes.size()));
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */
```
```JavaScript []
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 */
var Solution = function(head) {
    this.nodes = new Array()
    while(head!=null){
        this.nodes.push(head.val)
        head = head.next
    }
};

/**
 * @return {number}
 */
Solution.prototype.getRandom = function() {
    return this.nodes[Math.floor(Math.random() * this.nodes.length)]
};

/**
 * Your Solution object will be instantiated and called as such:
 * var obj = new Solution(head)
 * var param_1 = obj.getRandom()
 */
```
```Go []
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
type Solution struct {
    Nodes []int
}

func Constructor(head *ListNode) Solution {
    nodes := make([]int, 0)
    for head != nil {
        nodes = append(nodes, head.Val)
        head = head.Next
    }
    return Solution{nodes}
}

func (this *Solution) GetRandom() int {
    return this.Nodes[rand.Intn(len(this.Nodes))]
}
/**
 * Your Solution object will be instantiated and called as such:
 * obj := Constructor(head);
 * param_1 := obj.GetRandom();
 */
```
蓄水池抽样
```C 
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */



typedef struct {
    struct ListNode* root;
} Solution;


Solution* solutionCreate(struct ListNode* head) {
    Solution * obj = (Solution *)malloc(sizeof(Solution));
    obj->root = head;
    return obj;
}

int solutionGetRandom(Solution* obj) {
    struct ListNode* node = obj->root;
    int ans = 0;
    for(int i=1;node!=NULL;i++){
        if(rand()%i == 0)
            ans = node->val;
        node = node->next;
    }
    return ans;
}

void solutionFree(Solution* obj) {
    free(obj);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(head);
 * int param_1 = solutionGetRandom(obj);
 
 * solutionFree(obj);
*/
```