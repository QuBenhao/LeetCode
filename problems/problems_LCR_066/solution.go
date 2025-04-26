package problemLCR_066

import (
	"encoding/json"
	"log"
	"strings"
)

type TrieNode struct {
	Children map[rune]*TrieNode
	IsEnd    bool
	Value    int
}

func TrieNodeConstructor() *TrieNode {
	return &TrieNode{
		Children: make(map[rune]*TrieNode),
		IsEnd:    false,
	}
}

type MapSum struct {
	root *TrieNode
}

/** Initialize your data structure here. */
func Constructor() MapSum {
	return MapSum{root: TrieNodeConstructor()}
}

func (this *MapSum) Insert(key string, val int) {
	node := this.root
	for _, ch := range key {
		if _, ok := node.Children[ch]; !ok {
			node.Children[ch] = TrieNodeConstructor()
		}
		node = node.Children[ch]
	}
	node.IsEnd = true
	node.Value = val
}

func (this *MapSum) dfs(node *TrieNode) int {
	sum := 0
	if node.IsEnd {
		sum += node.Value
	}
	for _, child := range node.Children {
		sum += this.dfs(child)
	}
	return sum
}

func (this *MapSum) Sum(prefix string) int {
	node := this.root
	for _, ch := range prefix {
		if _, ok := node.Children[ch]; !ok {
			return 0
		}
		node = node.Children[ch]
	}
	return this.dfs(node)
}

/**
 * Your MapSum object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(key,val);
 * param_2 := obj.Sum(prefix);
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
		case "insert", "Insert":
			res = nil
			obj.Insert(opValues[i][0].(string), int(opValues[i][1].(float64)))
		case "sum", "Sum":
			res = obj.Sum(opValues[i][0].(string))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
