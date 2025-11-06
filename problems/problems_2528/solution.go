package problem2528

import (
	"encoding/json"
	"log"
	"strings"
)

func maxPower(stations []int, r int, k int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var stations []int
	var r int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &stations); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &r); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return maxPower(stations, r, k)
}
