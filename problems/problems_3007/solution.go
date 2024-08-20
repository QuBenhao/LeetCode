package problem3007

import (
	"encoding/json"
	"log"
	"strings"
)

func findMaximumNumber(k int64, x int) int64 {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var k int64
	var x int

	if err := json.Unmarshal([]byte(inputValues[0]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &x); err != nil {
		log.Fatal(err)
	}

	return findMaximumNumber(k, x)
}
