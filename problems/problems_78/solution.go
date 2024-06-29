package problem78

import (
	"encoding/json"
	"log"
	"strings"
)

func subsets(nums []int) [][]int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return subsets(nums)
}
