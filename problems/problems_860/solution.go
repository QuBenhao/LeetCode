package problem860

import (
	"encoding/json"
	"log"
	"strings"
)

func lemonadeChange(bills []int) bool {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var bills []int

	if err := json.Unmarshal([]byte(values[0]), &bills); err != nil {
		log.Fatal(err)
	}

	return lemonadeChange(bills)
}
