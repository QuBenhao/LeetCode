package problem1323

import (
	"encoding/json"
	"log"
	"strconv"
	"strings"
)

func maximum69Number(num int) int {
	s := []byte(strconv.Itoa(num))
	for i := range s {
		if s[i] == '6' {
			s[i] = '9'
			break
		}
	}
	result, _ := strconv.Atoi(string(s))
	return result
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var num int

	if err := json.Unmarshal([]byte(inputValues[0]), &num); err != nil {
		log.Fatal(err)
	}

	return maximum69Number(num)
}
