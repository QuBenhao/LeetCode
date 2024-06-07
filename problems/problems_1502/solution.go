package problem1502

import (
	"encoding/json"
	"log"
	"strings"
)

func canMakeArithmeticProgression(arr []int) bool {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var arr []int

	if err := json.Unmarshal([]byte(values[0]), &arr); err != nil {
		log.Fatal(err)
	}

	return canMakeArithmeticProgression(arr)
}
