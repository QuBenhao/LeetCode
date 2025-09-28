package problem1039

import (
	"encoding/json"
	"log"
	"strings"
)

func minScoreTriangulation(values []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var values []int

	if err := json.Unmarshal([]byte(inputValues[0]), &values); err != nil {
		log.Fatal(err)
	}

	return minScoreTriangulation(values)
}
