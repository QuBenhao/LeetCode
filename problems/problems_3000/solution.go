package problem3000

import (
	"encoding/json"
	"log"
	"strings"
)

func areaOfMaxDiagonal(dimensions [][]int) (ans int) {
	maxLength := 0
	for _, dimension := range dimensions {
		a, b := dimension[0], dimension[1]
		if length := a*a + b*b; length > maxLength {
			maxLength = length
			ans = a * b
		} else if length == maxLength {
			ans = max(ans, a*b)
		}
	}
	return
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var dimensions [][]int

	if err := json.Unmarshal([]byte(inputValues[0]), &dimensions); err != nil {
		log.Fatal(err)
	}

	return areaOfMaxDiagonal(dimensions)
}
