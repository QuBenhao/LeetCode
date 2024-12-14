package problem1338

import (
	"encoding/json"
	"log"
	"strings"
)

func minSetSize(arr []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return minSetSize(arr)
}
