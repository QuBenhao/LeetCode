package problem3582

import (
	"encoding/json"
	"log"
	"strings"
)

func generateTag(caption string) string {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var caption string

	if err := json.Unmarshal([]byte(inputValues[0]), &caption); err != nil {
		log.Fatal(err)
	}

	return generateTag(caption)
}
