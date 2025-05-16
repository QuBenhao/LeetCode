package problemLCR_057

import (
	"encoding/json"
	"log"
	"strings"
)

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var nums []int
	var k int
	var t int

	if err := json.Unmarshal([]byte(inputValues[0]), &nums); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &t); err != nil {
		log.Fatal(err)
	}

	return containsNearbyAlmostDuplicate(nums, k, t)
}
