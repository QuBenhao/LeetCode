package problem1128

import (
	"encoding/json"
	"log"
	"strings"
)

func numEquivDominoPairs(dominoes [][]int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var dominoes [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &dominoes); err != nil {
		log.Fatal(err)
	}

	return numEquivDominoPairs(dominoes)
}
