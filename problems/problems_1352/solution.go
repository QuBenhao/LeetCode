package problem1352

import (
	"encoding/json"
	"log"
	"strings"
)

type ProductOfNumbers struct {
    
}


func Constructor() ProductOfNumbers {
    
}


func (this *ProductOfNumbers) Add(num int)  {
    
}


func (this *ProductOfNumbers) GetProduct(k int) int {
    
}


/**
 * Your ProductOfNumbers object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(num);
 * param_2 := obj.GetProduct(k);
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
	obj := Constructor()
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "add", "Add":
			res = nil
			obj.Add(int(opValues[i][0].(float64)))
		case "getProduct", "GetProduct":
			res = obj.GetProduct(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
