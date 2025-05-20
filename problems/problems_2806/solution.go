package problem2806

import (
	"encoding/json"
	"log"
	"strings"
)

func accountBalanceAfterPurchase(purchaseAmount int) int {
	return 100 - (purchaseAmount+5)/10*10
}

func Solve(input string) any {
	values := strings.Split(input, "\n")
	var purchaseAmount int

	if err := json.Unmarshal([]byte(values[0]), &purchaseAmount); err != nil {
		log.Fatal(err)
	}

	return accountBalanceAfterPurchase(purchaseAmount)
}
