package problem146

import (
	"encoding/json"
	"log"
	"strings"
)

type DLinkedNode struct {
	key, value int
	prev, next *DLinkedNode
}

type LRUCache struct {
	capacity int
	cache    map[int]*DLinkedNode
	head     *DLinkedNode
	tail     *DLinkedNode
}

func Constructor(capacity int) LRUCache {
	lru := LRUCache{
		capacity: capacity,
		cache:    map[int]*DLinkedNode{},
		head:     &DLinkedNode{},
		tail:     &DLinkedNode{},
	}
	lru.head.next = lru.tail
	lru.tail.prev = lru.head
	return lru
}

func (this *LRUCache) moveToHead(node *DLinkedNode) {
	if node.prev != nil {
		node.prev.next = node.next
	}
	if node.next != nil {
		node.next.prev = node.prev
	}
	node.prev = this.head
	node.next = this.head.next

	this.head.next.prev = node
	this.head.next = node
}

func (this *LRUCache) removeNode(node *DLinkedNode) {
	node.prev.next = node.next
	node.next.prev = node.prev
}

func (this *LRUCache) Get(key int) int {
	if node, ok := this.cache[key]; ok {
		this.moveToHead(node)
		return node.value
	}
	return -1
}

func (this *LRUCache) Put(key int, value int) {
	if node, ok := this.cache[key]; ok {
		node.value = value
		this.moveToHead(node)
		return
	}
	if len(this.cache) == this.capacity {
		delete(this.cache, this.tail.prev.key)
		this.removeNode(this.tail.prev)
	}
	node := &DLinkedNode{key: key, value: value}
	this.cache[key] = node
	this.moveToHead(node)
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
