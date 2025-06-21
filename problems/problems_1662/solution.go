package problem1662

import (
	"encoding/json"
	"log"
	"strings"
)

func arrayStringsAreEqual(word1 []string, word2 []string) bool {
	m, n := len(word1), len(word2)
	idx1, idx2 := 0, 0
	i1, i2 := 0, 0
	for idx1 < m && idx2 < n {
		for i1 < len(word1[idx1]) && i2 < len(word2[idx2]) {
			if word1[idx1][i1] != word2[idx2][i2] {
				return false
			}
			i1++
			i2++
		}
		if i1 == len(word1[idx1]) {
			idx1++
			i1 = 0
		}
		if i2 == len(word2[idx2]) {
			idx2++
			i2 = 0
		}
	}
	return idx1 == m && idx2 == n
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var word1 []string
	var word2 []string

	if err := json.Unmarshal([]byte(inputValues[0]), &word1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &word2); err != nil {
		log.Fatal(err)
	}

	return arrayStringsAreEqual(word1, word2)
}
