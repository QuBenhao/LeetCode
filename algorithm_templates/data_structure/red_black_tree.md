# Red-Black Tree

- A **red-black tree** is a self-balancing binary search tree. It uses colors and rotations to maintain balance, ensuring **O(log n)** time complexity for insertion, deletion, and lookup.
- Core properties
    1. **Color rule**: Every node is either red or black.
    2. **Root**: The root must be black.
    3. **Leaves**: All leaves (NIL nodes) are black.
    4. **Red node constraint**: A red node must have black children (no consecutive red nodes).
    5. **Equal black height**: Every path from a given node to any of its leaves contains the same number of black nodes.
- [855. Exam Room](./problems/problems_855/solution.go)

```python
class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color='BLACK')  # Sentinel leaf node
        self.root = self.NIL

    def left_rotate(self, x):
        """ Left rotation to maintain red-black tree balance. """
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        """ Right rotation, mirroring the left rotation. """
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fixup(self, z):
        """ Repair colors and structure after insertion. """
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # Uncle node
                if y.color == 'RED':  # Case 1: The uncle is red
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:  # Case 2: Convert a triangle into a line
                        z = z.parent
                        self.left_rotate(z)
                    # Case 3: Recolor and rotate
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:  # Mirror the logic when the parent is a right child
                # TODO: Similar to the left-side logic ...
                pass
            if z == self.root:
                break
        self.root.color = 'BLACK'

    def insert(self, key):
        """ Insert a node and repair the tree. """
        z = Node(key)
        z.parent = self.NIL
        z.left = self.NIL
        z.right = self.NIL
        y = self.NIL
        x = self.root
        while x != self.NIL:  # Standard BST insertion
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z
        z.color = 'RED'
        self.insert_fixup(z)


# Usage example
rbt = RedBlackTree()
rbt.insert(10)
rbt.insert(20)
rbt.insert(5)
```

```go
package main

type Node struct {
	key    int
	color  bool // true: red, false: black
	left   *Node
	right  *Node
	parent *Node
}

const (
	RED   = true
	BLACK = false
)

type RedBlackTree struct {
	root *Node
	nil  *Node // Sentinel node
}

func NewRedBlackTree() *RedBlackTree {
	nilNode := &Node{color: BLACK}
	return &RedBlackTree{
		root: nilNode,
		nil:  nilNode,
	}
}

func (t *RedBlackTree) leftRotate(x *Node) {
	y := x.right
	x.right = y.left
	if y.left != t.nil {
		y.left.parent = x
	}
	y.parent = x.parent
	if x.parent == t.nil {
		t.root = y
	} else if x == x.parent.left {
		x.parent.left = y
	} else {
		x.parent.right = y
	}
	y.left = x
	x.parent = y
}

func (t *RedBlackTree) rightRotate(y *Node) {
	x := y.left
	y.left = x.right
	if x.right != t.nil {
		x.right.parent = y
	}
	x.parent = y.parent
	if y.parent == t.nil {
		t.root = x
	} else if y == y.parent.right {
		y.parent.right = x
	} else {
		y.parent.left = x
	}
	x.right = y
	y.parent = x
}

func (t *RedBlackTree) insertFixup(z *Node) {
	for z.parent.color == RED {
		if z.parent == z.parent.parent.left {
			y := z.parent.parent.right
			if y.color == RED {
				z.parent.color = BLACK
				y.color = BLACK
				z.parent.parent.color = RED
				z = z.parent.parent
			} else {
				if z == z.parent.right {
					z = z.parent
					t.leftRotate(z)
				}
				z.parent.color = BLACK
				z.parent.parent.color = RED
				t.rightRotate(z.parent.parent)
			}
		} else {
			y := z.parent.parent.left
			if y.color == RED {
				z.parent.color = BLACK
				y.color = BLACK
				z.parent.parent.color = RED
				z = z.parent.parent
			} else {
				if z == z.parent.left {
					z = z.parent
					t.rightRotate(z)
				}
				z.parent.color = BLACK
				z.parent.parent.color = RED
				t.leftRotate(z.parent.parent)
			}
		}
	}
	t.root.color = BLACK
}

func (t *RedBlackTree) Insert(key int) {
	z := &Node{
		key:    key,
		color:  RED,
		left:   t.nil,
		right:  t.nil,
		parent: t.nil,
	}
	y := t.nil
	x := t.root
	for x != t.nil {
		y = x
		if z.key < x.key {
			x = x.left
		} else {
			x = x.right
		}
	}
	z.parent = y
	if y == t.nil {
		t.root = z
	} else if z.key < y.key {
		y.left = z
	} else {
		y.right = z
	}
	t.insertFixup(z)
}

func (t *RedBlackTree) transplant(u, v *Node) {
	if u.parent == t.nil {
		t.root = v
	} else if u == u.parent.left {
		u.parent.left = v
	} else {
		u.parent.right = v
	}
	v.parent = u.parent
}

func (t *RedBlackTree) deleteFixup(x *Node) {
	for x != t.root && x.color == BLACK {
		if x == x.parent.left {
			w := x.parent.right
			if w.color == RED {
				w.color = BLACK
				x.parent.color = RED
				t.leftRotate(x.parent)
				w = x.parent.right
			}
			if w.left.color == BLACK && w.right.color == BLACK {
				w.color = RED
				x = x.parent
			} else {
				if w.right.color == BLACK {
					w.left.color = BLACK
					w.color = RED
					t.rightRotate(w)
					w = x.parent.right
				}
				w.color = x.parent.color
				x.parent.color = BLACK
				w.right.color = BLACK
				t.leftRotate(x.parent)
				x = t.root
			}
		} else {
			w := x.parent.left
			if w.color == RED {
				w.color = BLACK
				x.parent.color = RED
				t.rightRotate(x.parent)
				w = x.parent.left
			}
			if w.right.color == BLACK && w.left.color == BLACK {
				w.color = RED
				x = x.parent
			} else {
				if w.left.color == BLACK {
					w.right.color = BLACK
					w.color = RED
					t.leftRotate(w)
					w = x.parent.left
				}
				w.color = x.parent.color
				x.parent.color = BLACK
				w.left.color = BLACK
				t.rightRotate(x.parent)
				x = t.root
			}
		}
	}
	x.color = BLACK
}

func (t *RedBlackTree) Delete(key int) {
	z := t.root
	for z != t.nil && z.key != key {
		if key < z.key {
			z = z.left
		} else {
			z = z.right
		}
	}
	if z == t.nil {
		return
	}

	y := z
	yOriginalColor := y.color
	var x *Node
	if z.left == t.nil {
		x = z.right
		t.transplant(z, z.right)
	} else if z.right == t.nil {
		x = z.left
		t.transplant(z, z.left)
	} else {
		y = t.minimum(z.right)
		yOriginalColor = y.color
		x = y.right
		if y.parent == z {
			x.parent = y
		} else {
			t.transplant(y, y.right)
			y.right = z.right
			y.right.parent = y
		}
		t.transplant(z, y)
		y.left = z.left
		y.left.parent = y
		y.color = z.color
	}
	if yOriginalColor == BLACK {
		t.deleteFixup(x)
	}
}

func (t *RedBlackTree) minimum(x *Node) *Node {
	for x.left != t.nil {
		x = x.left
	}
	return x
}

func (t *RedBlackTree) InOrder() []int {
	var result []int
	t.inOrderHelper(t.root, &result)
	return result
}

func (t *RedBlackTree) inOrderHelper(node *Node, result *[]int) {
	if node != t.nil {
		t.inOrderHelper(node.left, result)
		*result = append(*result, node.key)
		t.inOrderHelper(node.right, result)
	}
}
```

## Key Operations Explained

| Operation | Description |
|----------|--------------------------------------------|
| **Left rotation** | Promote the right child to the parent position and make the original parent its left child, preserving the binary search tree property. |
| **Right rotation** | Promote the left child to the parent position and make the original parent its right child, mirroring the left rotation. |
| **Insertion fixup** | Resolve consecutive red nodes through recoloring and rotations. There are three cases, with the strategy determined by the uncle's color. |
| **Deletion fixup** | Resolve double-black nodes based on the sibling's color and its children (the code is complex, so the full logic is not shown). |

## Use Cases

1. **Ordered maps and sets**: Examples include Java's `TreeMap` and C++'s `std::map`.
2. **Database indexes**: B+ tree variants are often used for database indexes, while red-black trees manage data in memory.
3. **Task scheduling**: The Linux kernel's Completely Fair Scheduler (CFS) uses red-black trees to manage process queues.

Implementing a red-black tree helps explain the design of self-balancing data structures. In practice, use ordered containers from the language's standard library (such as Python's
`sortedcontainers` or the third-party Go library `github.com/emirpasic/gods/trees/redblacktree`).

