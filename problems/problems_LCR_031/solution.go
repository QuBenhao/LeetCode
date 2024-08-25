package problemLCR_031

import (
	"encoding/json"
	"log"
	"strings"
)

type DoublyListNode struct {
	Key   int
	Value int
	Prev  *DoublyListNode
	Next  *DoublyListNode
}

func newDoublyListNode(key, value int) *DoublyListNode {
	return &DoublyListNode{
		Key:   key,
		Value: value,
	}
}

func (dln *DoublyListNode) insert(node *DoublyListNode) {
	node.Prev = dln
	node.Next = dln.Next
	if dln.Next != nil {
		dln.Next.Prev = node
	}
	dln.Next = node
}

func removeNode(node *DoublyListNode) {
	node.Prev.Next = node.Next
	node.Next.Prev = node.Prev
}

type LRUCache struct {
	Capacity int
	Head     *DoublyListNode
	Tail     *DoublyListNode
	Hash     map[int]*DoublyListNode
}

func Constructor(capacity int) LRUCache {
	head := newDoublyListNode(-1, -1)
	tail := newDoublyListNode(-1, -1)
	head.Next = tail
	tail.Prev = head
	return LRUCache{
		Capacity: capacity,
		Head:     head,
		Tail:     tail,
		Hash:     make(map[int]*DoublyListNode),
	}
}

func (this *LRUCache) Get(key int) int {
	if node, ok := this.Hash[key]; ok {
		removeNode(node)
		this.Head.insert(node)
		return node.Value
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	var node *DoublyListNode
	if nd, ok := this.Hash[key]; ok {
		nd.Value = value
		removeNode(nd)
		node = nd
	} else {
		if len(this.Hash) == this.Capacity {
			delete(this.Hash, this.Tail.Prev.Key)
			removeNode(this.Tail.Prev)
		}
		node = newDoublyListNode(key, value)
		this.Hash[key] = node
	}
	this.Head.insert(node)
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
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
		case "get", "Get":
			res = obj.Get(int(opValues[i][0].(float64)))
		case "put", "Put":
			res = nil
			obj.Put(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
