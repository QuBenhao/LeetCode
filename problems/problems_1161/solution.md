# [Python/Java/TypeScript/Go] BFS

> Author: Benhao
> Date: 2022-07-30
> Upvotes: 25
> Tags: Go, Java, JavaScript, Python, Python3, TypeScript

---

### 解题思路
BFS统计每一层的和，返回和最大且层数最小的那个即可。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans, num, queue, level = 1, -inf, deque([root]), 1
        while queue:
            s = 0
            for i in range(len(queue)):
                node = queue.popleft()
                s += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if s > num:
                ans, num = level, s
            level += 1
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
    public int maxLevelSum(TreeNode root) {
        int ans = 1, num = Integer.MIN_VALUE, level = 1;
        Deque<TreeNode> queue = new ArrayDeque<>();
        queue.addLast(root);
        while(!queue.isEmpty()) {
            int sum = 0;
            for (int i = 0, size = queue.size(); i < size; i++) {
                TreeNode node = queue.removeFirst();
                sum += node.val;
                if (node.left != null) {
                    queue.addLast(node.left);
                }
                if (node.right != null) {
                    queue.addLast(node.right);
                }
            }
            if (sum > num) {
                ans = level;
                num = sum;
            }
            level++;
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

function maxLevelSum(root: TreeNode | null): number {
    let ans: number = 1, num: number = Number.MIN_SAFE_INTEGER, level: number = 1, queue: MyQueue<TreeNode> = new MyQueue<TreeNode>()
    queue.enqueue(root)
    while (!queue.isEmpty()) {
        let sum = 0
        for (let i = 0, size = queue.length; i < size; i++) {
            const node = queue.dequeue()
            sum += node.val
            if (node.left != null) {
                queue.enqueue(node.left)
            }
            if (node.right != null) {
                queue.enqueue(node.right)
            }
        }
        if (sum > num) {
            ans = level
            num = sum
        }
        level++
    }
    return ans
};

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
func maxLevelSum(root *TreeNode) int {
    ans, num, level, queue := 1, -int(1E9), 1, []*TreeNode{root}
    for len(queue) > 0 {
        size, sum := len(queue), 0
        for i := 0; i < size; i++ {
            sum += queue[i].Val
            if queue[i].Left != nil {
                queue = append(queue, queue[i].Left)
            }
            if queue[i].Right != nil {
                queue = append(queue, queue[i].Right)
            }
        }
        if (sum > num) {
            ans, num = level, sum
        }
        queue = queue[size:]
        level++
    }
    return ans
}
```