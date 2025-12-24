package problem3075

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumHappinessSum(happiness []int, k int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var happiness []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &happiness); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return maximumHappinessSum(happiness, k)
}
