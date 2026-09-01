package problem3875

import (
	"encoding/json"
	"log"
	"strings"
)

func uniformArray(nums1 []int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums1 []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums1); err != nil {
		log.Fatal(err)
	}

	return uniformArray(nums1)
}
