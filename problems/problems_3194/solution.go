package problem3194

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumAverage(nums []int) float64 {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}

	return minimumAverage(nums)
}
