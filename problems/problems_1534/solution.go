package problem1534

import (
	"encoding/json"
	"log"
	"strings"
)

func countGoodTriplets(arr []int, a int, b int, c int) int {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int
	var a int
	var b int
	var c int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &a); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &b); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &c); err != nil {
		log.Fatal(err)
	}

	return countGoodTriplets(arr, a, b, c)
}
