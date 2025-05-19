package problem3024

import (
	"encoding/json"
	"log"
	"strings"
)

func triangleType(nums []int) string {
	a, b, c := nums[0], nums[1], nums[2]
	mn, mx := min(a, b, c), max(a, b, c)
	remain := a + b + c - mx - mn
	if mx >= mn+remain {
		return "none"
	}
	if a == b && a == c {
		return "equilateral"
	}
	if a == b || a == c || b == c {
		return "isosceles"
	}
	return "scalene"
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return triangleType(nums)
}
