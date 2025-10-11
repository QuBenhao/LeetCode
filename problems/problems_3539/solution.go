package problem3539

import (
	"encoding/json"
	"log"
	"strings"
)

func magicalSum(m int, k int, nums []int) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var m int
	var k int
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &nums); err != nil {
		log.Fatal(err)
	}

	return magicalSum(m, k, nums)
}
