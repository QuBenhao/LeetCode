package problem2241

import (
	"encoding/json"
	"log"
	"strings"
)

type ATM struct {
    
}


func Constructor() ATM {
    
}


func (this *ATM) Deposit(banknotesCount []int)  {
    
}


func (this *ATM) Withdraw(amount int) []int {
    
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
