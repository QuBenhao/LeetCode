package problem11

import (
	"encoding/json"
	"log"
	"strings"
)

func maxArea(height []int) (ans int) {
	for i, j := 0, len(height)-1; i < j; {
		ans = max(ans, min(height[i], height[j])*(j-i))
		if height[i] > height[j] {
			j--
		} else {
			i++
		}
	}
	return
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var height []int

	if err := json.Unmarshal([]byte(values[0]), &height); err != nil {
		log.Fatal(err)
	}

	return maxArea(height)
}
