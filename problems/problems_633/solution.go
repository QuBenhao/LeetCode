package problem633

import (
	"encoding/json"
	"log"
	"strings"
)

func judgeSquareSum(c int) bool {
    
}

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var c int

	if err := json.Unmarshal([]byte(inputValues[0]), &c); err != nil {
		log.Fatal(err)
	}

	return judgeSquareSum(c)
}
