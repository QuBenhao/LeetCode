package problem55

import (
	"encoding/json"
	"log"
	"strings"
)

func canJump(nums []int) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return canJump(nums)
}
