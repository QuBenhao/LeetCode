package problem2073

import (
	"encoding/json"
	"log"
	"strings"
)

func timeRequiredToBuy(tickets []int, k int) int {
	ans, ticketToBuy := 0, tickets[k]
	for i, ticket := range tickets {
		if i <= k {
			ans += min(ticket, ticketToBuy)
		} else {
			ans += min(ticket, ticketToBuy-1)
		}
	}
	return ans
}

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var tickets []int
	var k int

	if err := json.Unmarshal([]byte(inputValues[0]), &tickets); err != nil {
		log.Fatal(err)
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &k); err != nil {
		log.Fatal(err)
	}

	return timeRequiredToBuy(tickets, k)
}
