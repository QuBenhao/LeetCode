package problem3360

import (
	"encoding/json"
	"log"
	"strings"
)

func canAliceWin(n int) bool {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &n); err != nil {
		log.Fatal(err)
	}

	return canAliceWin(n)
}
