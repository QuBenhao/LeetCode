package problem2976

import (
	"encoding/json"
	"log"
	"strings"
)

func minimumCost(source string, target string, original []byte, changed []byte, cost []int) int64 {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var source string
	var target string
	var original []byte
	var changed []byte
	var cost []int

	if err := json.Unmarshal([]byte(inputValues[0]), &source); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &target); err != nil {
		log.Fatal(err)
	}
	var originalStr []string
	if err := json.Unmarshal([]byte(inputValues[2]), &originalStr); err != nil {
		log.Fatal(err)
	}
	original = make([]byte, len(originalStr))
	for i := 0; i < len(original); i++ {
		original[i] = originalStr[i][0]
	}
	var changedStr []string
	if err := json.Unmarshal([]byte(inputValues[3]), &changedStr); err != nil {
		log.Fatal(err)
	}
	changed = make([]byte, len(changedStr))
	for i := 0; i < len(changed); i++ {
		changed[i] = changedStr[i][0]
	}
	if err := json.Unmarshal([]byte(inputValues[4]), &cost); err != nil {
		log.Fatal(err)
	}

	return minimumCost(source, target, original, changed, cost)
}

func byteArrToStrArr(arr []byte) []string {
	ans := make([]string, len(arr))
	for i, b := range arr {
		ans[i] = string(b)
	}
	return ans
}
