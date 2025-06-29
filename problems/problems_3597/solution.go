package problem3597

import (
	"encoding/json"
	"log"
	"strings"
)

type TrieNode struct {
	children map[byte]*TrieNode
	isEnd    bool
}

func TrieNodeConstructor() *TrieNode {
	return &TrieNode{children: make(map[byte]*TrieNode)}
}

func (t *TrieNode) SearchAndInsert(word string, i, j int) int {
	node := t
	for k := i; k <= j; k++ {
		c := word[k]
		if _, exists := node.children[c]; !exists {
			node.children[c] = TrieNodeConstructor()
			node.children[c].isEnd = true
			return k + 1
		}
		node = node.children[c]
	}
	if node.isEnd {
		return -1
	}
	return j + 1
}

func partitionString(s string) (ans []string) {
	root := TrieNodeConstructor()
	n := len(s)
	for i := 0; i < n; {
		j := root.SearchAndInsert(s, i, n-1)
		if j == -1 {
			break
		}
		ans = append(ans, s[i:j])
		i = j
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}

	return partitionString(s)
}
