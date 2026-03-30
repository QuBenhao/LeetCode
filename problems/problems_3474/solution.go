package problem3474

import (
	"encoding/json"
	"log"
	"strings"
)

func generateString(str1 string, str2 string) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var str1 string
	var str2 string

	if err := json.Unmarshal([]byte(inputValues[0]), &str1); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &str2); err != nil {
		log.Fatal(err)
	}

	return generateString(str1, str2)
}
