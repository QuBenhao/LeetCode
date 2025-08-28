package problem565

import (
	"encoding/json"
	"log"
	"strings"
)

func arrayNesting(nums []int) (ans int) {
	n := len(nums)
	visited := make([]bool, n)
	for i := range n {
		if visited[i] {
			continue
		}
		visited[i] = true
		cur, j := 1, nums[i]
		for j != i {
			visited[j] = true
			j = nums[j]
			cur++
		}
		ans = max(ans, cur)
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return arrayNesting(nums)
}
