package problemInterview_10__01

import (
	"encoding/json"
	"log"
	"strings"
)

func merge(A []int, m int, B []int, n int)  {
    
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var A []int
	var m int
	var B []int
	var n int

	if err := json.Unmarshal([]byte(inputValues[0]), &A); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &m); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[2]), &B); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[3]), &n); err != nil {
		log.Fatal(err)
	}

	merge(A, m, B, n)
	return A
}
