package problemLCR_034

import (
	"encoding/json"
	"log"
	"strings"
)

func isAlienSorted(words []string, order string) bool {
	orderMap := make(map[byte]int)
	for i := 0; i < len(order); i++ {
		orderMap[order[i]] = i
	}
	for i := 0; i < len(words)-1; i++ {
		idx := 0
		for idx < len(words[i]) && idx < len(words[i+1]) {
			if v0, v1 := orderMap[words[i][idx]], orderMap[words[i+1][idx]]; v0 > v1 {
				return false
			} else if v0 < v1 {
				break
			}
			idx++
		}
		if idx == len(words[i+1]) && idx < len(words[i]) {
			return false
		}
	}
	return true
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var words []string
	var order string

	if err := json.Unmarshal([]byte(inputValues[0]), &words); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &order); err != nil {
		log.Fatal(err)
	}

	return isAlienSorted(words, order)
}
