package problemLCR_064

import (
	"encoding/json"
	"log"
	"strings"
)

type TrieNode struct {
	children [26]*TrieNode
	isEnd    bool
}

func (t *TrieNode) query(word string, index int, change bool) bool {
	if index == len(word) {
		return change && t.isEnd
	}
	if !change {
		for i := 0; i < 26; i++ {
			if word[index] == byte(i+'a') {
				continue
			}
			if t.children[i] != nil && t.children[i].query(word, index+1, true) {
				return true
			}
		}
	}
	return t.children[word[index]-'a'] != nil && t.children[word[index]-'a'].query(word, index+1, change)
}

type MagicDictionary struct {
	root *TrieNode
}

// Constructor /** Initialize your data structure here. */
func Constructor() MagicDictionary {
	return MagicDictionary{root: &TrieNode{}}
}

func (md *MagicDictionary) BuildDict(dictionary []string) {
	for _, word := range dictionary {
		node := md.root
		for _, ch := range word {
			if node.children[ch-'a'] == nil {
				node.children[ch-'a'] = &TrieNode{}
			}
			node = node.children[ch-'a']
		}
		node.isEnd = true
	}
}

func (md *MagicDictionary) Search(searchWord string) bool {
	return md.root.query(searchWord, 0, false)
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
