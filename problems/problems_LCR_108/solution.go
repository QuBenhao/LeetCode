package problemLCR_108

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func ladderLength(beginWord string, endWord string, wordList []string) int {
	wordId := map[string]int{}
	graph := [][]int{}
	addWord := func(word string) int {
		id, has := wordId[word]
		if !has {
			id = len(wordId)
			wordId[word] = id
			graph = append(graph, []int{})
		}
		return id
	}
	addEdge := func(word string) int {
		id1 := addWord(word)
		s := []byte(word)
		for i, b := range s {
			s[i] = '*'
			id2 := addWord(string(s))
			graph[id1] = append(graph[id1], id2)
			graph[id2] = append(graph[id2], id1)
			s[i] = b
		}
		return id1
	}

	for _, word := range wordList {
		addEdge(word)
	}
	beginId := addEdge(beginWord)
	endId, has := wordId[endWord]
	if !has {
		return 0
	}

	const inf int = math.MaxInt64
	distBegin := make([]int, len(wordId))
	for i := range distBegin {
		distBegin[i] = inf
	}
	distBegin[beginId] = 0
	queueBegin := []int{beginId}

	distEnd := make([]int, len(wordId))
	for i := range distEnd {
		distEnd[i] = inf
	}
	distEnd[endId] = 0
	queueEnd := []int{endId}

	for len(queueBegin) > 0 && len(queueEnd) > 0 {
		q := queueBegin
		queueBegin = nil
		for _, v := range q {
			if distEnd[v] < inf {
				return (distBegin[v]+distEnd[v])/2 + 1
			}
			for _, w := range graph[v] {
				if distBegin[w] == inf {
					distBegin[w] = distBegin[v] + 1
					queueBegin = append(queueBegin, w)
				}
			}
		}

		q = queueEnd
		queueEnd = nil
		for _, v := range q {
			if distBegin[v] < inf {
				return (distBegin[v]+distEnd[v])/2 + 1
			}
			for _, w := range graph[v] {
				if distEnd[w] == inf {
					distEnd[w] = distEnd[v] + 1
					queueEnd = append(queueEnd, w)
				}
			}
		}
	}
	return 0
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var beginWord string
	var endWord string
	var wordList []string

	if err := json.Unmarshal([]byte(inputValues[0]), &beginWord); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &endWord); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &wordList); err != nil {
		log.Fatal(err)
	}

	return ladderLength(beginWord, endWord, wordList)
}
