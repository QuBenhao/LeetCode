package problem2043

import (
	"encoding/json"
	"log"
	"strings"
)

type Bank struct {
    
}


func Constructor(balance []int64) Bank {
    
}


func (this *Bank) Transfer(account1 int, account2 int, money int64) bool {
    
}


func (this *Bank) Deposit(account int, money int64) bool {
    
}


func (this *Bank) Withdraw(account int, money int64) bool {
    
}


/**
 * Your Bank object will be instantiated and called as such:
 * obj := Constructor(balance);
 * param_1 := obj.Transfer(account1,account2,money);
 * param_2 := obj.Deposit(account,money);
 * param_3 := obj.Withdraw(account,money);
 */

func Solve(inputJsonValues string) any {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]any
	var ans []any
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	obj := Constructor(opValues[0][0].([]int64))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "transfer", "Transfer":
			res = obj.Transfer(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)), opValues[i][2].(int64))
		case "deposit", "Deposit":
			res = obj.Deposit(int(opValues[i][0].(float64)), opValues[i][1].(int64))
		case "withdraw", "Withdraw":
			res = obj.Withdraw(int(opValues[i][0].(float64)), opValues[i][1].(int64))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
