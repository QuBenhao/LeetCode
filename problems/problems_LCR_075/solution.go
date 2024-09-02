package problemLCR_075

import (
	"encoding/json"
	"log"
	"strings"
)

func relativeSortArray(arr1 []int, arr2 []int) []int {

}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var arr1 []int
	var arr2 []int

	if err := json.Unmarshal([]byte(inputValues[0]), &arr1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &arr2); err != nil {
		log.Fatal(err)
	}

	return relativeSortArray(arr1, arr2)
}
