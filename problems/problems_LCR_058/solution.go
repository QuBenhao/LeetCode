package problemLCR_058

import (
	"encoding/json"
	"log"
	"strings"
)

type Node struct {
	left, right *Node
	val, lazy   int
}

type DynamicSegmentTree struct {
	root       *Node
	start, end int
}

func NewDynamicSegmentTree(start, end int) *DynamicSegmentTree {
	return &DynamicSegmentTree{
		root:  &Node{},
		start: start,
		end:   end,
	}
}

func (dst *DynamicSegmentTree) pushDown(node *Node) {
	if node.left == nil {
		node.left = &Node{}
	}
	if node.right == nil {
		node.right = &Node{}
	}
	if node.lazy != 0 {
		// 更新左子节点
		node.left.val = node.lazy
		node.left.lazy = node.lazy
		// 更新右子节点
		node.right.val = node.lazy
		node.right.lazy = node.lazy
		node.lazy = 0
	}
}

func (dst *DynamicSegmentTree) update(node *Node, l, r, ul, ur, val int) {
	if ul <= l && r <= ur {
		node.val = val
		node.lazy = val
		return
	}
	dst.pushDown(node)
	mid := (l + r) / 2
	if ul <= mid {
		dst.update(node.left, l, mid, ul, ur, val)
	}
	if ur > mid {
		dst.update(node.right, mid+1, r, ul, ur, val)
	}
	node.val = max(node.left.val, node.right.val)
}

func (dst *DynamicSegmentTree) UpdateRange(l, r, val int) {
	dst.update(dst.root, dst.start, dst.end, l, r, val)
}

func (dst *DynamicSegmentTree) query(node *Node, l, r, ql, qr int) int {
	if qr < l || r < ql {
		return 0
	}
	if ql <= l && r <= qr {
		return node.val
	}
	dst.pushDown(node)
	mid := (l + r) / 2
	return max(dst.query(node.left, l, mid, ql, qr),
		dst.query(node.right, mid+1, r, ql, qr))
}

func (dst *DynamicSegmentTree) QueryRange(l, r int) int {
	return dst.query(dst.root, dst.start, dst.end, l, r)
}

type MyCalendar struct {
	tree *DynamicSegmentTree
}

func Constructor() MyCalendar {
	return MyCalendar{
		tree: NewDynamicSegmentTree(0, 1000_000_000),
	}
}

func (mc *MyCalendar) Book(start int, end int) bool {
	if mc.tree.QueryRange(start, end-1) > 0 {
		return false
	}
	mc.tree.UpdateRange(start, end-1, 1)
	return true
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(start,end);
 */

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]any
	var ans []any
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	obj := Constructor()
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "book", "Book":
			res = obj.Book(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
