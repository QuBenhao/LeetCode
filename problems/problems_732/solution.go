package problem732

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

func (dst *DynamicSegmentTree) pushDown(node *Node, l, r int) {
	if node.left == nil {
		node.left = &Node{}
	}
	if node.right == nil {
		node.right = &Node{}
	}
	if node.lazy != 0 {
		// 更新左子节点
		node.left.val += node.lazy
		node.left.lazy += node.lazy
		// 更新右子节点
		node.right.val += node.lazy
		node.right.lazy += node.lazy
		node.lazy = 0
	}
}

func (dst *DynamicSegmentTree) update(node *Node, l, r, ul, ur, val int) {
	if ul <= l && r <= ur {
		node.val += val
		node.lazy += val
		return
	}
	dst.pushDown(node, l, r)
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
	dst.pushDown(node, l, r)
	mid := (l + r) / 2
	return max(dst.query(node.left, l, mid, ql, qr),
		dst.query(node.right, mid+1, r, ql, qr))
}

func (dst *DynamicSegmentTree) QueryRange(l, r int) int {
	return dst.query(dst.root, dst.start, dst.end, l, r)
}

type MyCalendarThree struct {
	tree DynamicSegmentTree
}

func Constructor() MyCalendarThree {
	return MyCalendarThree{
		*NewDynamicSegmentTree(0, 1e9),
	}
}

func (this *MyCalendarThree) Book(startTime int, endTime int) int {
	this.tree.UpdateRange(startTime, endTime-1, 1)
	return this.tree.QueryRange(0, 1e9)
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Book(startTime,endTime);
 */

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]interface{}
	var ans []interface{}
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
		var res interface{}
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
