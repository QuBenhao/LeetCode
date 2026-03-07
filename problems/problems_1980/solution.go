package problem1980

import (
	"encoding/json"
	"log"
	"strings"
)

func findDifferentBinaryString(nums []string) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []string

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return findDifferentBinaryString(nums)
}
