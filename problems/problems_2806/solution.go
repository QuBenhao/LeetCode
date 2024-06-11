package problem2806

import (
	"encoding/json"
	"log"
	"strings"
)

func accountBalanceAfterPurchase(purchaseAmount int) int {

}

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var purchaseAmount int

	if err := json.Unmarshal([]byte(values[0]), &purchaseAmount); err != nil {
		log.Fatal(err)
	}

	return accountBalanceAfterPurchase(purchaseAmount)
}
