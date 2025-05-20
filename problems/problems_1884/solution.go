package problem1884

import (
	"encoding/json"
	"log"
	"math"
	"strings"
)

func twoEggDrop(n int) int {
	return int(math.Ceil(math.Sqrt(float64(n*8+1)))) / 2
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return twoEggDrop(n)
}
