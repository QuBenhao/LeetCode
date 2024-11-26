package problem3208

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfAlternatingGroups(colors []int, k int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var colors []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &colors); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return numberOfAlternatingGroups(colors, k)
}
