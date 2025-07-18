package problem1233

import (
	"encoding/json"
	"log"
	"strings"
)

func removeSubfolders(folder []string) []string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var folder []string

	if err := json.Unmarshal([]byte(inputValues[0]), &folder); err != nil {
		log.Fatal(err)
	}

	return removeSubfolders(folder)
}
