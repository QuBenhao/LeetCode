package problem1111

import (
	"encoding/json"
	"log"
	"strings"
)

func maxDepthAfterSplit(seq string) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var seq string

	if err := json.Unmarshal([]byte(inputValues[0]), &seq); err != nil {
		log.Fatal(err)
	}

	return maxDepthAfterSplit(seq)
}
