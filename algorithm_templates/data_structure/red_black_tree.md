# 红黑树

- **红黑树**是一种自平衡的二叉搜索树，通过颜色标记和旋转操作保持平衡，确保插入、删除和查找的时间复杂度为 **O(log n)**。
- 核心性质
    1. **颜色规则**：每个节点是红色或黑色。
    2. **根节点**：根必须是黑色。
    3. **叶子节点**：所有叶子（NIL节点）是黑色。
    4. **红色节点限制**：红色节点的子节点必须是黑色（无连续红节点）。
    5. **黑高一致**：从任意节点到其所有叶子节点的路径中，黑色节点数量相同。
- [855. 考场就座](./problems/problems_855/solution.go)

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
        self.NIL = Node(None, color='BLACK')  # 哨兵叶子节点
        self.root = self.NIL

    def left_rotate(self, x):
        """ 左旋操作（维护红黑树平衡） """
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
        """ 右旋操作（镜像对称） """
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
        """ 插入后修复颜色和结构 """
        while z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # 叔节点
                if y.color == 'RED':  # Case 1: 叔节点为红
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:  # Case 2: 三角结构转直线
                        z = z.parent
                        self.left_rotate(z)
                    # Case 3: 调整颜色并旋转
                    z.parent.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    self.right_rotate(z.parent.parent)
            else:  # 镜像处理父节点在右侧的情况
                # TODO: 类似左侧逻辑 ...
                pass
            if z == self.root:
                break
        self.root.color = 'BLACK'

    def insert(self, key):
        """ 插入节点并修复 """
        z = Node(key)
        z.parent = self.NIL
        z.left = self.NIL
        z.right = self.NIL
        y = self.NIL
        x = self.root
        while x != self.NIL:  # 标准BST插入
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


# 使用示例
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

## 关键操作解析

| 操作       | 说明                                         |
|----------|--------------------------------------------|
| **左旋**   | 将右子节点提升为父节点，原父节点变为左子节点，保持二叉搜索树性质。          |
| **右旋**   | 将左子节点提升为父节点，原父节点变为右子节点，镜像对称操作。             |
| **插入修复** | 通过颜色翻转和旋转解决连续红节点问题，分三种情况处理（叔节点颜色决定策略）。     |
| **删除修复** | 处理双重黑节点问题，通过兄弟节点颜色和子节点分布调整（代码较复杂，未展示完整逻辑）。 |

## 应用场景

1. **有序映射/集合**：如Java的`TreeMap`、C++的`std::map`。
2. **数据库索引**：B+树的变种常用于数据库索引，红黑树用于内存数据管理。
3. **任务调度**：Linux内核的公平调度器（CFS）用红黑树管理进程队列。

通过实现红黑树，可以深入理解自平衡数据结构的设计思想，但实际开发中建议直接使用语言标准库中的有序容器（如Python的
`sortedcontainers`或Golang的第三方库`github.com/emirpasic/gods/trees/redblacktree`）。

