package problem855

import (
	"encoding/json"
	"log"
	"strings"
)

type Segment struct {
	start       int
	end         int
	maxDistance int
}

func (s Segment) Less(than Item) bool {
	if s.maxDistance == than.(Segment).maxDistance {
		return s.start > than.(Segment).start
	}
	return s.maxDistance < than.(Segment).maxDistance
}

type ExamRoom struct {
	rb             *Rbtree
	startToSegment map[int]Segment
	endToSegment   map[int]Segment
	n              int
}

func Constructor(n int) ExamRoom {
	rb := New()
	rb.Init()
	newSegment := Segment{-1, n, n - 1}
	rb.Insert(newSegment)
	startToSegment, endToSegment := make(map[int]Segment), make(map[int]Segment)
	startToSegment[-1] = newSegment
	endToSegment[n] = newSegment
	return ExamRoom{rb, startToSegment, endToSegment, n}
}

func (this *ExamRoom) getMaxDistance(start, end int) int {
	if start == -1 {
		return end - 1
	} else if end == this.n {
		return this.n - start - 2
	} else {
		return (end-start)/2 - 1
	}
}

func (this *ExamRoom) Seat() int {
	maxSeg := this.rb.Max().(Segment)
	if maxSeg.maxDistance < 0 {
		return -1
	}
	this.rb.Delete(maxSeg)
	start, end := maxSeg.start, maxSeg.end
	var p int
	if start == -1 {
		p = 0
	} else if end == this.n {
		p = this.n - 1
	} else {
		p = start + (end-start)/2
	}
	left, right := Segment{start, p, this.getMaxDistance(start, p)}, Segment{p, end, this.getMaxDistance(p, end)}
	this.rb.Insert(left)
	this.rb.Insert(right)
	this.startToSegment[start] = left
	this.startToSegment[p] = right
	this.endToSegment[end] = right
	this.endToSegment[p] = left
	return p
}

func (this *ExamRoom) Leave(p int) {
	left, right := this.endToSegment[p], this.startToSegment[p]
	delete(this.startToSegment, p)
	delete(this.endToSegment, p)
	newSegment := Segment{left.start, right.end, this.getMaxDistance(left.start, right.end)}
	this.startToSegment[left.start] = newSegment
	this.endToSegment[right.end] = newSegment
	this.rb.Delete(left)
	this.rb.Delete(right)
	this.rb.Insert(newSegment)
}

func (t *Rbtree) Len() uint { return t.count }

// Insert func inserts a item as a new RED node
func (t *Rbtree) Insert(item Item) {
	if item == nil {
		return
	}

	// Always insert a RED node
	t.insert(&Node{t.NIL, t.NIL, t.NIL, RED, item})
}

// InsertOrGet inserts or retrieves the item in the tree. If the
// item is already in the tree then the return value will be that.
// If the item is not in the tree the return value will be the item
// you put in.
func (t *Rbtree) InsertOrGet(item Item) Item {
	if item == nil {
		return nil
	}

	return t.insert(&Node{t.NIL, t.NIL, t.NIL, RED, item}).Item
}

// Delete delete the item in the tree
func (t *Rbtree) Delete(item Item) Item {
	if item == nil {
		return nil
	}

	// The `color` field here is nobody
	return t.delete(&Node{t.NIL, t.NIL, t.NIL, RED, item}).Item
}

// Get search for the specified items which is carried by a Node
func (t *Rbtree) Get(item Item) Item {
	if item == nil {
		return nil
	}

	// The `color` field here is nobody
	ret := t.search(&Node{t.NIL, t.NIL, t.NIL, RED, item})
	if ret == nil {
		return nil
	}

	return ret.Item
}

// Search does only search the node which includes it node
// TODO: This is for debug, delete it in the future
func (t *Rbtree) Search(item Item) *Node {

	return t.search(&Node{t.NIL, t.NIL, t.NIL, RED, item})
}

// Min return the item minimum one
func (t *Rbtree) Min() Item {
	x := t.min(t.root)

	if x == t.NIL {
		return nil
	}

	return x.Item
}

// Max return the item maxmum one
func (t *Rbtree) Max() Item {
	x := t.max(t.root)

	if x == t.NIL {
		return nil
	}

	return x.Item
}

type Node struct {
	Left   *Node
	Right  *Node
	Parent *Node
	Color  uint

	// for use by client.
	Item
}

const (
	// RED represents the color of the node is red
	RED = 0
	// BLACK represents the color of the node is black
	BLACK = 1
)

// Item has a method to compare items which is less
type Item interface {
	Less(than Item) bool
}

// Rbtree represents a Red-Black tree.
type Rbtree struct {
	NIL   *Node
	root  *Node
	count uint
}

func less(x, y Item) bool {
	return x.Less(y)
}

// New returns an initialized Red-Black tree
func New() *Rbtree { return new(Rbtree).Init() }

// Init returns the initial of rbtree
func (t *Rbtree) Init() *Rbtree {
	node := &Node{nil, nil, nil, BLACK, nil}
	return &Rbtree{
		NIL:   node,
		root:  node,
		count: 0,
	}
}

func (t *Rbtree) leftRotate(x *Node) {
	// Since we are doing the left rotation, the right child should *NOT* nil.
	if x.Right == t.NIL {
		return
	}

	//
	// The illation of left rotation
	//
	//          |                                  |
	//          X                                  Y
	//         / \         left rotate            / \
	//        α  Y       ------------->         X   γ
	//           / \                            / \
	//          β  γ                         α  β
	//
	// It should be note that during the rotating we do not change
	// the Nodes' color.
	//
	y := x.Right
	x.Right = y.Left
	if y.Left != t.NIL {
		y.Left.Parent = x
	}
	y.Parent = x.Parent

	if x.Parent == t.NIL {
		t.root = y
	} else if x == x.Parent.Left {
		x.Parent.Left = y
	} else {
		x.Parent.Right = y
	}

	y.Left = x
	x.Parent = y
}

func (t *Rbtree) rightRotate(x *Node) {
	// Since we are doing the right rotation, the left child should *NOT* nil.
	if x.Left == t.NIL {
		return
	}

	//
	// The illation of right rotation
	//
	//          |                                  |
	//          X                                  Y
	//         / \         right rotate           / \
	//        Y   γ      ------------->         α  X
	//       / \                                    / \
	//      α  β                                 β  γ
	//
	// It should be note that during the rotating we do not change
	// the Nodes' color.
	//
	y := x.Left
	x.Left = y.Right
	if y.Right != t.NIL {
		y.Right.Parent = x
	}
	y.Parent = x.Parent

	if x.Parent == t.NIL {
		t.root = y
	} else if x == x.Parent.Left {
		x.Parent.Left = y
	} else {
		x.Parent.Right = y
	}

	y.Right = x
	x.Parent = y
}

func (t *Rbtree) insert(z *Node) *Node {
	x := t.root
	y := t.NIL

	for x != t.NIL {
		y = x
		if less(z.Item, x.Item) {
			x = x.Left
		} else if less(x.Item, z.Item) {
			x = x.Right
		} else {
			return x
		}
	}

	z.Parent = y
	if y == t.NIL {
		t.root = z
	} else if less(z.Item, y.Item) {
		y.Left = z
	} else {
		y.Right = z
	}

	t.count++
	t.insertFixup(z)
	return z
}

func (t *Rbtree) insertFixup(z *Node) {
	for z.Parent.Color == RED {
		//
		// Howerver, we do not need the assertion of non-nil grandparent
		// because
		//
		//  2) The root is black
		//
		// Since the color of the parent is RED, so the parent is not root
		// and the grandparent must be exist.
		//
		if z.Parent == z.Parent.Parent.Left {
			// Take y as the uncle, although it can be NIL, in that case
			// its color is BLACK
			y := z.Parent.Parent.Right
			if y.Color == RED {
				//
				// Case 1:
				// Parent and uncle are both RED, the grandparent must be BLACK
				// due to
				//
				//  4) Both children of every red node are black
				//
				// Since the current node and its parent are all RED, we still
				// in violation of 4), So repaint both the parent and the uncle
				// to BLACK and grandparent to RED(to maintain 5)
				//
				//  5) Every simple path from root to leaves contains the same
				//     number of black nodes.
				//
				z.Parent.Color = BLACK
				y.Color = BLACK
				z.Parent.Parent.Color = RED
				z = z.Parent.Parent
			} else {
				if z == z.Parent.Right {
					//
					// Case 2:
					// Parent is RED and uncle is BLACK and the current node
					// is right child
					//
					// A left rotation on the parent of the current node will
					// switch the roles of each other. This still leaves us in
					// violation of 4).
					// The continuation into Case 3 will fix that.
					//
					z = z.Parent
					t.leftRotate(z)
				}
				//
				// Case 3:
				// Parent is RED and uncle is BLACK and the current node is
				// left child
				//
				// At the very beginning of Case 3, current node and parent are
				// both RED, thus we violate 4).
				// Repaint parent to BLACK will fix it, but 5) does not allow
				// this because all paths that go through the parent will get
				// 1 more black node. Then repaint grandparent to RED (as we
				// discussed before, the grandparent is BLACK) and do a right
				// rotation will fix that.
				//
				z.Parent.Color = BLACK
				z.Parent.Parent.Color = RED
				t.rightRotate(z.Parent.Parent)
			}
		} else { // same as then clause with "right" and "left" exchanged
			y := z.Parent.Parent.Left
			if y.Color == RED {
				z.Parent.Color = BLACK
				y.Color = BLACK
				z.Parent.Parent.Color = RED
				z = z.Parent.Parent
			} else {
				if z == z.Parent.Left {
					z = z.Parent
					t.rightRotate(z)
				}
				z.Parent.Color = BLACK
				z.Parent.Parent.Color = RED
				t.leftRotate(z.Parent.Parent)
			}
		}
	}
	t.root.Color = BLACK
}

// Just traverse the node from root to left recursively until left is NIL.
// The node whose left is NIL is the node with minimum value.
func (t *Rbtree) min(x *Node) *Node {
	if x == t.NIL {
		return t.NIL
	}

	for x.Left != t.NIL {
		x = x.Left
	}

	return x
}

// Just traverse the node from root to right recursively until right is NIL.
// The node whose right is NIL is the node with maximum value.
func (t *Rbtree) max(x *Node) *Node {
	if x == t.NIL {
		return t.NIL
	}

	for x.Right != t.NIL {
		x = x.Right
	}

	return x
}

func (t *Rbtree) search(x *Node) *Node {
	p := t.root

	for p != t.NIL {
		if less(p.Item, x.Item) {
			p = p.Right
		} else if less(x.Item, p.Item) {
			p = p.Left
		} else {
			break
		}
	}

	return p
}

// TODO: Need Document
func (t *Rbtree) successor(x *Node) *Node {
	if x == t.NIL {
		return t.NIL
	}

	// Get the minimum from the right sub-tree if it existed.
	if x.Right != t.NIL {
		return t.min(x.Right)
	}

	y := x.Parent
	for y != t.NIL && x == y.Right {
		x = y
		y = y.Parent
	}
	return y
}

// TODO: Need Document
func (t *Rbtree) delete(key *Node) *Node {
	z := t.search(key)

	if z == t.NIL {
		return t.NIL
	}
	ret := &Node{t.NIL, t.NIL, t.NIL, z.Color, z.Item}

	var y *Node
	var x *Node

	if z.Left == t.NIL || z.Right == t.NIL {
		y = z
	} else {
		y = t.successor(z)
	}

	if y.Left != t.NIL {
		x = y.Left
	} else {
		x = y.Right
	}

	// Even if x is NIL, we do the assign. In that case all the NIL nodes will
	// change from {nil, nil, nil, BLACK, nil} to {nil, nil, ADDR, BLACK, nil},
	// but do not worry about that because it will not affect the compare
	// between Node-X with Node-NIL
	x.Parent = y.Parent

	if y.Parent == t.NIL {
		t.root = x
	} else if y == y.Parent.Left {
		y.Parent.Left = x
	} else {
		y.Parent.Right = x
	}

	if y != z {
		z.Item = y.Item
	}

	if y.Color == BLACK {
		t.deleteFixup(x)
	}

	t.count--

	return ret
}

func (t *Rbtree) deleteFixup(x *Node) {
	for x != t.root && x.Color == BLACK {
		if x == x.Parent.Left {
			w := x.Parent.Right
			if w.Color == RED {
				w.Color = BLACK
				x.Parent.Color = RED
				t.leftRotate(x.Parent)
				w = x.Parent.Right
			}
			if w.Left.Color == BLACK && w.Right.Color == BLACK {
				w.Color = RED
				x = x.Parent
			} else {
				if w.Right.Color == BLACK {
					w.Left.Color = BLACK
					w.Color = RED
					t.rightRotate(w)
					w = x.Parent.Right
				}
				w.Color = x.Parent.Color
				x.Parent.Color = BLACK
				w.Right.Color = BLACK
				t.leftRotate(x.Parent)
				// this is to exit while loop
				x = t.root
			}
		} else { // the code below is has left and right switched from above
			w := x.Parent.Left
			if w.Color == RED {
				w.Color = BLACK
				x.Parent.Color = RED
				t.rightRotate(x.Parent)
				w = x.Parent.Left
			}
			if w.Left.Color == BLACK && w.Right.Color == BLACK {
				w.Color = RED
				x = x.Parent
			} else {
				if w.Left.Color == BLACK {
					w.Right.Color = BLACK
					w.Color = RED
					t.leftRotate(w)
					w = x.Parent.Left
				}
				w.Color = x.Parent.Color
				x.Parent.Color = BLACK
				w.Left.Color = BLACK
				t.rightRotate(x.Parent)
				x = t.root
			}
		}
	}
	x.Color = BLACK
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Seat();
 * obj.Leave(p);
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
	obj := Constructor(int(opValues[0][0].(float64)))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "seat", "Seat":
			res = obj.Seat()
		case "leave", "Leave":
			res = nil
			obj.Leave(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
