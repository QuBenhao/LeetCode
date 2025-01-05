package problem2274

import (
	"encoding/json"
	"log"
	"strings"
)

func maxConsecutive(bottom int, top int, special []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var bottom int
	var top int
	var special []int

	if err := json.Unmarshal([]byte(inputValues[0]), &bottom); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &top); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &special); err != nil {
		log.Fatal(err)
	}

	return maxConsecutive(bottom, top, special)
}
