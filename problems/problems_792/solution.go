package problem792

import (
	"encoding/json"
	"log"
	"strings"
)

func numMatchingSubseq(s string, words []string) (ans int) {
	idxMap := make(map[rune][]int, 26)
	for i, c := range s {
		idxMap[c] = append(idxMap[c], i)
	}
	for _, word := range words {
		idx := 0
		sIdx := -1
		m := len(word)
		for idx < m {
			curList := idxMap[rune(word[idx])]
			left, right := 0, len(curList)
			for left < right {
				mid := left + (right-left)/2
				if curList[mid] < sIdx+1 {
					left = mid + 1
				} else {
					right = mid
				}
			}
			if left == len(curList) {
				break
			}
			sIdx = curList[left]
			idx++
		}
		if idx == m {
			ans++
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var words []string

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &words); err != nil {
		log.Fatal(err)
	}

	return numMatchingSubseq(s, words)
}
