package problem1385

import (
	"encoding/json"
	"log"
	"strings"
)

func findTheDistanceValue(arr1 []int, arr2 []int, d int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr1 []int
	var arr2 []int
	var d int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &arr2); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &d); err != nil {
		log.Fatal(err)
	}

	return findTheDistanceValue(arr1, arr2, d)
}
