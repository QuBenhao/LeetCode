package problemLCR_067

import (
	"encoding/json"
	"log"
	"strings"
)

type Trie struct {
	children [2]*Trie
}

func (t *Trie) insert(num int) {
	var node = t
	for i := 31; i >= 0; i-- {
		bit := (num >> i) & 1
		if node.children[bit] == nil {
			node.children[bit] = &Trie{}
		}
		node = node.children[bit]
	}
}

func (t *Trie) search(num int) (ans int) {
	var node = t
	for i := 31; i >= 0; i-- {
		bit := (num >> i) & 1
		if node.children[bit^1] != nil {
			ans |= 1 << i
			node = node.children[bit^1]
			continue
		}
		if node.children[bit] == nil {
			return -1
		}
		node = node.children[bit]
	}
	return
}

func findMaximumXOR(nums []int) (ans int) {
	root := &Trie{}
	for _, num := range nums {
		ans = max(ans, root.search(num))
		root.insert(num)
	}
	return
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return findMaximumXOR(nums)
}
