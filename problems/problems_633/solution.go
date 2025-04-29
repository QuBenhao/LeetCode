package problem633

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func judgeSquareSum(c int) bool {
	i, j := 0, int(math.Sqrt(float64(c)))
	for i <= j {
		if s := i*i + j*j; s == c {
			return true
		} else if s > c {
			j--
		} else {
			i++
		}
	}
	return false
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var c int

	if err := json.Unmarshal([]byte(inputValues[0]), &c); err != nil {
		log.Fatal(err)
	}

	return judgeSquareSum(c)
}
