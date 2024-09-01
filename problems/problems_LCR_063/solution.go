package problemLCR_063

import (
	"encoding/json"
	"log"
	"strings"
)

type Trie struct {
	children [26]*Trie
	isEnd    bool
}

func Constructor() Trie {
	return Trie{}
}

func (t *Trie) Insert(word string) {
	node := t
	for _, ch := range word {
		ch -= 'a'
		if node.children[ch] == nil {
			node.children[ch] = &Trie{}
		}
		node = node.children[ch]
	}
	node.isEnd = true
}

func (t *Trie) FindPrefix(word string) string {
	node := t
	for i, ch := range word {
		ch -= 'a'
		if node.isEnd {
			return word[:i]
		}
		if node.children[ch] == nil {
			break
		}
		node = node.children[ch]
	}
	return word
}

func replaceWords(dictionary []string, sentence string) string {
	trie := Constructor()
	for _, word := range dictionary {
		trie.Insert(word)
	}
	words := strings.Split(sentence, " ")
	for i, word := range words {
		words[i] = trie.FindPrefix(word)
	}
	return strings.Join(words, " ")
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var dictionary []string
	var sentence string

	if err := json.Unmarshal([]byte(inputValues[0]), &dictionary); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &sentence); err != nil {
		log.Fatal(err)
	}

	return replaceWords(dictionary, sentence)
}
