package problem3242

import (
	"encoding/json"
	"log"
	"strings"
)

type NeighborSum struct {
    
}


func Constructor(grid [][]int) NeighborSum {
    
}


func (this *NeighborSum) AdjacentSum(value int) int {
    
}


func (this *NeighborSum) DiagonalSum(value int) int {
    
}


/**
 * Your NeighborSum object will be instantiated and called as such:
 * obj := Constructor(grid);
 * param_1 := obj.AdjacentSum(value);
 * param_2 := obj.DiagonalSum(value);
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
		case "adjacentSum", "AdjacentSum":
			res = obj.AdjacentSum(int(opValues[i][0].(float64)))
		case "diagonalSum", "DiagonalSum":
			res = obj.DiagonalSum(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
