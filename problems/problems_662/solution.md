# [Python/Java/TypeScript/Go] BFS

> Author: Benhao
> Date: 2022-08-26
> Upvotes: 25
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
使用满二叉树编号, 可以轻松计算同一层任意两节点的距离(带空节点), 我们BFS返回最左和最右距离最大的那层即可。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans, queue = 0, deque([(1, root)])
        while queue:
            mn, mx = inf, 0
            for _ in range(len(queue)):
                code, node = queue.popleft()
                if node.left:
                    queue.append((code * 2, node.left))
                if node.right:
                    queue.append((code * 2 + 1, node.right))
                mn, mx = min(code, mn), max(code, mx)
            ans = max(ans, mx - mn + 1)
        return ans
```
```Java []
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int widthOfBinaryTree(TreeNode root) {
        int ans = 0;
        Deque<Pair<Integer, TreeNode>> queue = new ArrayDeque<>();
        queue.addLast(new Pair<>(1, root));
        while (!queue.isEmpty()) {
            int max = 0, min = 0;
            for (int i = 0, n = queue.size(); i < n; i++) {
                Pair<Integer, TreeNode> pair = queue.removeFirst();
                int code = pair.getKey();
                TreeNode node = pair.getValue();
                if (i == 0) {
                    min = code;
                } 
                if (i == n - 1) {
                    max = code;
                }
                if (node.left != null) {
                    queue.addLast(new Pair<>(code << 1, node.left));
                }
                if (node.right != null) {
                    queue.addLast(new Pair<>((code << 1) + 1, node.right));
                }
            }
            ans = Math.max(ans, max - min + 1);
        }
        return ans;
    }

}
```
```TypeScript []
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function widthOfBinaryTree(root: TreeNode | null): number {
    let ans: bigint = 0n
    const queue: MyQueue<{a: bigint, b: TreeNode}> = new MyQueue<{a: bigint, b: TreeNode}>()
    queue.enqueue({a: 1n, b: root})
    while (!queue.isEmpty()) {
        const size: number = queue.length
        let min: bigint = 0n, max: bigint = 0n
        for (let i = 0; i < size; i++) {
            const {a: code, b: node} = queue.dequeue()
            if (i == 0) {
                min = code
            }
            if (i == size - 1) {
                max = code
            }
            if (node.left != null) {
                queue.enqueue({a: code * 2n, b: node.left})
            }
            if (node.right != null) {
                queue.enqueue({a: code * 2n + 1n, b: node.right})
            }
        }
        if (max - min + 1n > ans) {
            ans = max - min + 1n
        }
    }
    return Number(ans)
};

/**
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */

// https://github.com/yangshun/lago

export interface AbstractNode {
  next?: AbstractNode | null;
  prev?: AbstractNode | null;
}

class Node<T> implements AbstractNode {
  public value: T;

  public next: AbstractNode | null;

  public prev: AbstractNode | null;

  constructor(value: T) {
    this.value = value;
    this.next = null;
    this.prev = null;
  }
}

class DummyHeadNode implements AbstractNode {
  public next: AbstractNode | null;

  constructor() {
    this.next = null;
  }
}

class DummyTailNode implements AbstractNode {
  public prev: AbstractNode | null;

  constructor() {
    this.prev = null;
  }
}

class MyQueue<T> {
  private _dummyHead: DummyHeadNode;

  private _dummyTail: DummyTailNode;

  private _length: number;

  constructor() {
    this._dummyHead = new DummyHeadNode();
    this._dummyTail = new DummyTailNode();
    this._dummyHead.next = this._dummyTail;
    this._dummyTail.prev = this._dummyHead;
    this._length = 0;
  }

  /**
   * Adds an element to the back of the Queue.
   * @param {*} element
   * @return {number} The new length of the Queue.
   */
  enqueue(value: T): number {
    const node = new Node(value);
    const prevLast = this._dummyTail.prev as Node<T> | DummyHeadNode;
    prevLast.next = node;

    node.prev = prevLast;
    node.next = this._dummyTail;
    this._dummyTail.prev = node;
    this._length++;
    return this._length;
  }

  /**
   * Removes the element at the front of the Queue.
   * @return {*} The element at the front of the Queue.
   */
  dequeue(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }

    const node = this._dummyHead.next as Node<T>;
    const newFirst = node.next as Node<T> | DummyTailNode;
    this._dummyHead.next = newFirst;
    newFirst.prev = this._dummyHead;
    node.next = null;
    this._length--;
    return node.value;
  }

  /**
   * Returns true if the Queue has no elements.
   * @return {boolean} Whether the Queue has no elements.
   */
  isEmpty(): boolean {
    return this._length === 0;
  }

  /**
   * Returns the element at the front of the Queue.
   * @return {*} The element at the front of the Queue.
   */
  front(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }

    return (this._dummyHead.next as Node<T>).value;
  }

  /**
   * Returns the element at the back of the Queue.
   * @return {*} The element at the back of the Queue.
   */
  back(): T | undefined {
    if (this.isEmpty()) {
      return undefined;
    }

    return (this._dummyTail.prev as Node<T>).value;
  }

  /**
   * Returns the number of elements in the Queue.
   * @return {number} Number of elements in the Queue.
   */
  get length(): number {
    return this._length;
  }
}
```
```Go []
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func widthOfBinaryTree(root *TreeNode) (ans int) {
    queue := []Pair{Pair{1, root}}
    for size := len(queue); size > 0; size = len(queue) {
        min, max := 0, 0
        for i := 0; i < size; i++ {
            pair := queue[i]
            code, node := pair.Code, pair.Node
            if i == 0 {
                min = code
            }
            if i == size - 1 {
                max = code
            }
            if node.Left != nil {
                queue = append(queue, Pair{code << 1, node.Left})
            }
            if node.Right != nil {
                queue = append(queue, Pair{(code << 1) + 1, node.Right})
            }
        }
        queue = queue[size:]
        if d := max - min + 1; d > ans {
            ans = d
        }
    }
    return
}

type Pair struct {
    Code int
    Node *TreeNode
}
```