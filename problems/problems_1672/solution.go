package problem1672

import (
	"encoding/json"
	"log"
	"strings"
)

func maximumWealth(accounts [][]int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var accounts [][]int

	if err := json.Unmarshal([]byte(values[0]), &accounts); err != nil {
		log.Fatal(err)
	}

	return maximumWealth(accounts)
}
