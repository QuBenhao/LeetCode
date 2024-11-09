package problemLCR_039

import (
	"encoding/json"
	"log"
	"strings"
)

func largestRectangleArea(heights []int) int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var heights []int

	if err := json.Unmarshal([]byte(inputValues[0]), &heights); err != nil {
		log.Fatal(err)
	}

	return largestRectangleArea(heights)
}
