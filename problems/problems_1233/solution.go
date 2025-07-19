package problem1233

import (
	"encoding/json"
	"log"
	"slices"
	"strings"
)

func removeSubfolders(folder []string) (ans []string) {
	root := TrieNodeConstructor()
	slices.Sort(folder)
	for _, f := range folder {
		parts := strings.Split(f, "/")[1:]
		if !root.HasPrefix(parts) {
			root.Insert(parts)
			ans = append(ans, f)
		}
	}
	return
}

type TrieNode struct {
	children map[string]*TrieNode
	isEnd    bool
}

func TrieNodeConstructor() *TrieNode {
	return &TrieNode{children: make(map[string]*TrieNode)}
}

func (t *TrieNode) Insert(word []string) {
	node := t
	for _, char := range word {
		if _, exists := node.children[char]; !exists {
			node.children[char] = TrieNodeConstructor()
		}
		node = node.children[char]
	}
	node.isEnd = true
}

func (t *TrieNode) HasPrefix(word []string) bool {
	node := t
	for _, char := range word {
		if _, exists := node.children[char]; !exists {
			return false
		}
		node = node.children[char]
		if node.isEnd {
			return true
		}
	}
	return false
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var folder []string

	if err := json.Unmarshal([]byte(inputValues[0]), &folder); err != nil {
		log.Fatal(err)
	}

	return removeSubfolders(folder)
}
