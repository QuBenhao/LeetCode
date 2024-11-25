package problem3206

import (
	"encoding/json"
	"log"
	"strings"
)

func numberOfAlternatingGroups(colors []int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var colors []int

	if err := json.Unmarshal([]byte(inputValues[0]), &colors); err != nil {
		log.Fatal(err)
	}

	return numberOfAlternatingGroups(colors)
}
