package problem1128

import (
	"encoding/json"
	"log"
	"strings"
)

func numEquivDominoPairs(dominoes [][]int) (ans int) {
	counter := map[int]int{}
	for _, domino := range dominoes {
		d := max(domino[0], domino[1])*10 + min(domino[0], domino[1])
		ans += counter[d]
		counter[d]++
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var dominoes [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &dominoes); err != nil {
		log.Fatal(err)
	}

	return numEquivDominoPairs(dominoes)
}
