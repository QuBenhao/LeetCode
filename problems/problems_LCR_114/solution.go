package problemLCR_114

import (
	"encoding/json"
	"log"
	"strings"
)

func alienOrder(words []string) string {
	chars := make(map[byte]any)
	graph := make([][]int, 26)
	inDegree := make([]int, 26)

	build := func(word1, word2 string) bool {
		m, n := len(word1), len(word2)
		for i := 0; i < min(m, n); i++ {
			if word1[i] != word2[i] {
				u := word1[i] - 'a'
				v := word2[i] - 'a'
				graph[u] = append(graph[u], int(v))
				inDegree[v]++
				return true
			}
		}
		return m <= n
	}

	for i := 0; i < len(words[0]); i++ {
		chars[words[0][i]] = nil
	}
	for i := 0; i < len(words)-1; i++ {
		for j := 0; j < len(words[i+1]); j++ {
			chars[words[i+1][j]] = nil
		}
		if !build(words[i], words[i+1]) {
			return ""
		}
	}
	queue := make([]int, 0)
	for i := 0; i < 26; i++ {
		if _, exists := chars[byte(i+'a')]; !exists {
			continue
		}
		if inDegree[i] == 0 {
			queue = append(queue, i)
		}
	}
	result := make([]byte, 0)
	for len(queue) > 0 {
		u := queue[0]
		result = append(result, byte(u+'a'))
		queue = queue[1:]
		for _, v := range graph[u] {
			inDegree[v]--
			if inDegree[v] == 0 {
				queue = append(queue, v)
			}
		}
	}
	if len(chars) != len(result) {
		return ""
	}
	return string(result)
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}

	return alienOrder(words)
}
