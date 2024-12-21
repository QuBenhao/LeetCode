package problem1387

import (
	"encoding/json"
	"log"
	"strings"
)

func getKth(lo int, hi int, k int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var lo int
	var hi int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &lo); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &hi); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &k); err != nil {
		log.Fatal(err)
	}

	return getKth(lo, hi, k)
}
