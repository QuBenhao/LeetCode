package problem2078

import (
	"encoding/json"
	"log"
	"strings"
)

func maxDistance(colors []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var colors []int

	if err := json.Unmarshal([]byte(inputValues[0]), &colors); err != nil {
		log.Fatal(err)
	}

	return maxDistance(colors)
}
