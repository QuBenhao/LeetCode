package problem2766

import (
	"encoding/json"
	"log"
	"strings"
)

func relocateMarbles(nums []int, moveFrom []int, moveTo []int) []int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var moveFrom []int
	var moveTo []int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &moveFrom); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &moveTo); err != nil {
		log.Fatal(err)
	}

	return relocateMarbles(nums, moveFrom, moveTo)
}
