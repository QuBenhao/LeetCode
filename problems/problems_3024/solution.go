package problem3024

import (
	"encoding/json"
	"log"
	"strings"
)

func triangleType(nums []int) string {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return triangleType(nums)
}
