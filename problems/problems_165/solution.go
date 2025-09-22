package problem165

import (
	"encoding/json"
	"log"
	"strings"
)

func compareVersion(version1 string, version2 string) int {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var version1 string
	var version2 string

	if err := json.Unmarshal([]byte(inputValues[0]), &version1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &version2); err != nil {
		log.Fatal(err)
	}

	return compareVersion(version1, version2)
}
