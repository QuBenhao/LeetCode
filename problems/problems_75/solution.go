package problem75

import (
	"encoding/json"
	"log"
	"strings"
)

func sortColors(nums []int)  {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	sortColors(nums)
	return nums
}
