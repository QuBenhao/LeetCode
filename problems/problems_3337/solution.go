package problem3337

import (
	"encoding/json"
	"log"
	"strings"
)

func lengthAfterTransformations(s string, t int, nums []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var s string
	var t int
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &s); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &t); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &nums); err != nil {
		log.Fatal(err)
	}

	return lengthAfterTransformations(s, t, nums)
}
