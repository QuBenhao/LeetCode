package problemLCR_069

import (
	"encoding/json"
	"log"
	"strings"
)

func peakIndexInMountainArray(arr []int) int {

}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return peakIndexInMountainArray(arr)
}
