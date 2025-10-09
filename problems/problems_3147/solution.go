package problem3147

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumEnergy(energy []int, k int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var energy []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &energy); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maximumEnergy(energy, k)
}
