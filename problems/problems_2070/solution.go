package problem2070

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumBeauty(items [][]int, queries []int) []int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var items [][]int
	var queries []int

	if err := json.Unmarshal([]byte(inputValues[0]), &items); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &queries); err != nil {
		log.Fatal(err)
	}

	return maximumBeauty(items, queries)
}
