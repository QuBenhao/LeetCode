package problem1331

import (
	"encoding/json"
	"log"
	"strings"
)

func arrayRankTransform(arr []int) []int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return arrayRankTransform(arr)
}
