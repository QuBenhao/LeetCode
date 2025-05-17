package problemLCR_013

import (
	"encoding/json"
	"log"
	"strings"
)

type NumMatrix struct {
    
}


func Constructor(matrix [][]int) NumMatrix {
    
}


func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
    
}


/**
 * Your NumMatrix object will be instantiated and called as such:
 * obj := Constructor(matrix);
 * param_1 := obj.SumRegion(row1,col1,row2,col2);
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
	obj := Constructor(opValues[0][0].([][]int))
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "sumRegion", "SumRegion":
			res = obj.SumRegion(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)), int(opValues[i][2].(float64)), int(opValues[i][3].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
