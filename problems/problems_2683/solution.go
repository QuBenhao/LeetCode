package problem2683

import (
	"encoding/json"
	"log"
	"strings"
)

func doesValidArrayExist(derived []int) bool {
	a := 0
	for _, d := range derived {
		a ^= d
	}
	return a == 0
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var derived []int

	if err := json.Unmarshal([]byte(inputValues[0]), &derived); err != nil {
		log.Fatal(err)
	}

	return doesValidArrayExist(derived)
}
