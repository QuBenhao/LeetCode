package problem3200

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func f(n, m int) int {
	odd := int(math.Sqrt(float64(n)))
	even := int((math.Sqrt(float64(m*4+1)) - 1) / 2)
	if odd > even {
		return even*2 + 1
	}
	return odd * 2
}

func maxHeightOfTriangle(red, blue int) int {
	return max(f(red, blue), f(blue, red))
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var red int
	var blue int

	if err := json.Unmarshal([]byte(inputValues[0]), &red); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &blue); err != nil {
		log.Fatal(err)
	}

	return maxHeightOfTriangle(red, blue)
}
