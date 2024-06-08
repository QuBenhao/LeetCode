package problem312

import (
	"encoding/json"
	"log"
	"strings"
)

func maxCoins(nums []int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return maxCoins(nums)
}
