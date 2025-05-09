package problem2241

import (
	"encoding/json"
	"log"
	"strings"
)

var banknotes = []int{20, 50, 100, 200, 500}

type ATM struct {
	banknotesCount []int
}

func Constructor() ATM {
	return ATM{
		banknotesCount: make([]int, len(banknotes)),
	}
}

func (atm *ATM) Deposit(banknotesCount []int) {
	for i := 0; i < len(banknotesCount); i++ {
		atm.banknotesCount[i] += banknotesCount[i]
	}
}

func (atm *ATM) Withdraw(amount int) (ans []int) {
	defer func() {
		if ans[0] != -1 {
			for i, v := range ans {
				atm.banknotesCount[i] -= v
			}
		}
	}()
	tmp := make([]int, len(banknotes))
	for i := len(banknotes) - 1; i >= 0; i-- {
		if atm.banknotesCount[i] > 0 && amount >= banknotes[i] {
			tmp[i] = min(atm.banknotesCount[i], amount/banknotes[i])
			amount -= tmp[i] * banknotes[i]
		}
	}
	if amount > 0 {
		ans = append(ans, -1)
		return
	}
	ans = make([]int, len(banknotes))
	copy(ans, tmp)
	return
}

/**
 * Your ATM object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Deposit(banknotesCount);
 * param_2 := obj.Withdraw(amount);
 */

func Solve(inputJsonValues string) interface{} {
	inputValues := strings.Split(inputJsonValues, "\n")
	var operators []string
	var opValues [][]interface{}
	var ans []interface{}
	if err := json.Unmarshal([]byte(inputValues[0]), &operators); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(inputValues[1]), &opValues); err != nil {
		log.Println(err)
		return nil
	}
	obj := Constructor()
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "deposit", "Deposit":
			var arr []int
			if v, ok := opValues[i][0].([]int); ok {
				arr = v
			} else {
				for _, vi := range opValues[i][0].([]interface{}) {
					arr = append(arr, int(vi.(float64)))
				}
			}
			res = nil
			obj.Deposit(arr)
		case "withdraw", "Withdraw":
			res = obj.Withdraw(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}

	return ans
}
