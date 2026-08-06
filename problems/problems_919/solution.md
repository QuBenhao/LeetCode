# [Python/Java/TypeScript/Go] 队列

> slug: pythonjavatypescriptgo-by-himymben-3e9w
> date: 2022-07-24
> tags: Go, Java, JavaScript, Python, Python3, TypeScript
> question: Complete Binary Tree Inserter (complete-binary-tree-inserter)
> url: https://leetcode.cn/problems/complete-binary-tree-inserter/solutions/XtG97w/pythonjavatypescriptgo-by-himymben-3e9w/

---
### 解题思路
由于题目是完全二叉树且始终优先添左边，
整个填充过程是从上到下，从左到右的，这个顺序满足先进先出，故使用BFS + 队列。
当一个节点不是左右节点都有时，它就还是可以插入的节点，放入队列中，插入时最先进队列的节点优先添加子节点即可。

### 代码

```Python3 []
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = deque([])
        q = deque([root])
        while q:
            node = q.popleft()
            if not node.right or not node.left:
                self.queue.append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, val: int) -> int:
        if self.queue[0].left:
            node = self.queue.popleft()
            node.right = TreeNode(val)
            self.queue.append(node.right)
        else:
            node = self.queue[0]
            node.left = TreeNode(val)
            self.queue.append(node.left)
        return node.val

    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
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
class CBTInserter {
    private TreeNode root;
    private Deque<TreeNode> queue;
    public CBTInserter(TreeNode root) {
        this.root = root;
        queue = new ArrayDeque<>();
        Deque<TreeNode> q = new ArrayDeque<>();
        q.addLast(root);
        while(!q.isEmpty()) {
            var node = q.removeFirst();
            if (node.right == null || node.left == null) {
                queue.addLast(node);
            }
            if (node.left != null) {
                q.addLast(node.left);
            }
            if (node.right != null) {
                q.addLast(node.right);
            }
        }
    }
    
    public int insert(int val) {
        var node = queue.peekFirst();
        if (node.left == null) {
            node.left = new TreeNode(val);
            queue.addLast(node.left);
        } else {
            queue.removeFirst();
            node.right = new TreeNode(val);
            queue.addLast(node.right);
        }
        return node.val;
    }
    
    public TreeNode get_root() {
        return root;
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(val);
 * TreeNode param_2 = obj.get_root();
 */
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

class CBTInserter {
    root: TreeNode
    queue: MyQueue<TreeNode>
    constructor(root: TreeNode | null) {
        this.root = root
        this.queue = new MyQueue<TreeNode>()
        const q = new MyQueue<TreeNode>()
        q.enqueue(root)
        while (!q.isEmpty()) {
            const node = q.dequeue()
            if (node.right == null || node.left == null) {
                this.queue.enqueue(node)
            }
            if (node.left != null) {
                q.enqueue(node.left)
            }
            if (node.right != null) {
                q.enqueue(node.right)
            }
        }
    }

    insert(val: number): number {
        const node = this.queue.front()
        if (node.left == null) {
            node.left = new TreeNode(val)
            this.queue.enqueue(node.left)
        } else {
            this.queue.dequeue()
            node.right = new TreeNode(val)
            this.queue.enqueue(node.right)
        }
        return node.val
    }

    get_root(): TreeNode | null {
        return this.root
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * var obj = new CBTInserter(root)
 * var param_1 = obj.insert(val)
 * var param_2 = obj.get_root()
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
type CBTInserter struct {
    Root *TreeNode
    Queue []*TreeNode
}


func Constructor(root *TreeNode) CBTInserter {
    queue := []*TreeNode{}
    q := []*TreeNode{root}
    for len(q) > 0 {
        node := q[0]
        q = q[1:]
        if node.Right == nil || node.Left == nil {
            queue = append(queue, node)
        }
        if node.Left != nil {
            q = append(q, node.Left)
        }
        if node.Right != nil {
            q = append(q, node.Right)
        }
    }
    return CBTInserter{root, queue}
}


func (this *CBTInserter) Insert(val int) int {
    node := this.Queue[0]
    if node.Left == nil {
        node.Left = &TreeNode{val, nil, nil}
        this.Queue = append(this.Queue, node.Left)
    } else {
        this.Queue = this.Queue[1:]
        node.Right = &TreeNode{val, nil, nil}
        this.Queue = append(this.Queue, node.Right)
    }
    return node.Val
}


func (this *CBTInserter) Get_root() *TreeNode {
    return this.Root
}


/**
 * Your CBTInserter object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Insert(val);
 * param_2 := obj.Get_root();
 */
```