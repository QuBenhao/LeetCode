package problem75

import (
	"encoding/json"
	"log"
	"strings"
)

func sortColors(nums []int) {
	for i, p0, p1 := 0, 0, 0; i < len(nums); i++ {
		if nums[i] == 1 {
			nums[p1], nums[i] = nums[i], nums[p1]
			p1++
		} else if nums[i] == 0 {
			nums[p0], nums[i] = nums[i], nums[p0]
			if p0 < p1 {
				nums[p1], nums[i] = nums[i], nums[p1]
			}
			p0++
			p1++
		}
	}
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(values[0]), &nums); err != nil {
		log.Fatal(err)
	}

	sortColors(nums)
	return nums
}
