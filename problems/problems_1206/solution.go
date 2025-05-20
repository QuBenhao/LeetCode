package problem1206

import (
	"encoding/json"
	"log"
	"math/rand"
	"strings"
	"time"
)

const (
	maxLevel = 16  // 最大层数
	p        = 0.5 // 层数生成概率
)

type SkipNode struct {
	val  int
	next []*SkipNode
}

type Skiplist struct {
	head  *SkipNode
	level int
}

func Constructor() Skiplist {
	rand.Seed(time.Now().UnixNano())
	return Skiplist{
		head:  &SkipNode{next: make([]*SkipNode, maxLevel)},
		level: 0,
	}
}

func (sl *Skiplist) randomLevel() int {
	level := 1
	for rand.Float64() < p && level < maxLevel {
		level++
	}
	return level
}

func (sl *Skiplist) Search(target int) bool {
	curr := sl.head
	for i := sl.level - 1; i >= 0; i-- {
		for curr.next[i] != nil && curr.next[i].val < target {
			curr = curr.next[i]
		}
	}
	curr = curr.next[0]
	return curr != nil && curr.val == target
}

func (sl *Skiplist) Add(num int) {
	update := make([]*SkipNode, maxLevel)
	curr := sl.head
	for i := sl.level - 1; i >= 0; i-- {
		for curr.next[i] != nil && curr.next[i].val < num {
			curr = curr.next[i]
		}
		update[i] = curr
	}
	newLevel := sl.randomLevel()
	if newLevel > sl.level {
		for i := sl.level; i < newLevel; i++ {
			update[i] = sl.head
		}
		sl.level = newLevel
	}
	newNode := &SkipNode{
		val:  num,
		next: make([]*SkipNode, newLevel),
	}
	for i := 0; i < newLevel; i++ {
		newNode.next[i] = update[i].next[i]
		update[i].next[i] = newNode
	}
}

func (sl *Skiplist) Erase(num int) bool {
	update := make([]*SkipNode, maxLevel)
	curr := sl.head
	for i := sl.level - 1; i >= 0; i-- {
		for curr.next[i] != nil && curr.next[i].val < num {
			curr = curr.next[i]
		}
		update[i] = curr
	}
	curr = curr.next[0]
	if curr == nil || curr.val != num {
		return false
	}
	for i := 0; i < sl.level; i++ {
		if update[i].next[i] != curr {
			break
		}
		update[i].next[i] = curr.next[i]
	}
	for sl.level > 0 && sl.head.next[sl.level-1] == nil {
		sl.level--
	}
	return true
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Search(target);
 * obj.Add(num);
 * param_3 := obj.Erase(num);
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
		case "search", "Search":
			res = obj.Search(int(opValues[i][0].(float64)))
		case "add", "Add":
			res = nil
			obj.Add(int(opValues[i][0].(float64)))
		case "erase", "Erase":
			res = obj.Erase(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
