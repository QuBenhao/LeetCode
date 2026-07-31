package problem486

import (
	"encoding/json"
	"log"
	"strings"
)

func predictTheWinner(nums []int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return predictTheWinner(nums)
}
