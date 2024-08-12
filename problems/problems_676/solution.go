package problem676

import (
	"encoding/json"
	"log"
	"strings"
)

type TrieNode struct {
	children map[byte]*TrieNode
	isEnd    bool
}

func constructorTrie() *TrieNode {
	return &TrieNode{
		children: make(map[byte]*TrieNode),
		isEnd:    false,
	}
}

func query(node *TrieNode, word []byte, remain int) bool {
	if len(word) == 0 {
		return node.isEnd && remain == 0
	}
	if v, ok := node.children[word[0]]; ok {
		if query(v, word[1:], remain) {
			return true
		}
	}
	if remain == 0 {
		return false
	}
	remain--
	for k, v := range node.children {
		if k == word[0] {
			continue
		}
		if query(v, word[1:], remain) {
			return true
		}
	}
	return false
}

type MagicDictionary struct {
	root *TrieNode
}

func Constructor() MagicDictionary {
	return MagicDictionary{
		root: constructorTrie(),
	}
}

func (this *MagicDictionary) BuildDict(dictionary []string) {
	for _, word := range dictionary {
		node := this.root
		for i := 0; i < len(word); i++ {
			if _, ok := node.children[word[i]]; !ok {
				node.children[word[i]] = constructorTrie()
			}
			node = node.children[word[i]]
		}
		node.isEnd = true
	}
}

func (this *MagicDictionary) Search(searchWord string) bool {
	return query(this.root, []byte(searchWord), 1)
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.BuildDict(dictionary);
 * param_2 := obj.Search(searchWord);
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
		case "buildDict", "BuildDict":
			var arr []string
			if v, ok := opValues[i][0].([]string); ok {
				arr = v
			} else {
				for _, vi := range opValues[i][0].([]interface{}) {
					arr = append(arr, vi.(string))
				}
			}
			res = nil
			obj.BuildDict(arr)
		case "search", "Search":
			res = obj.Search(opValues[i][0].(string))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
