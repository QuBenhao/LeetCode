package problem2288

import (
	"encoding/json"
	"log"
	"strings"
)

func discountPrices(sentence string, discount int) string {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var sentence string
	var discount int

	if err := json.Unmarshal([]byte(values[0]), &sentence); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(values[1]), &discount); err != nil {
		log.Fatal(err)
	}

	return discountPrices(sentence, discount)
}
