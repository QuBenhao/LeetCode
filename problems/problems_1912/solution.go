package problem1912

import (
	"encoding/json"
	"log"
	"strings"
)

type MovieRentingSystem struct {
    
}


func Constructor(n int, entries [][]int) MovieRentingSystem {
    
}


func (this *MovieRentingSystem) Search(movie int) []int {
    
}


func (this *MovieRentingSystem) Rent(shop int, movie int)  {
    
}


func (this *MovieRentingSystem) Drop(shop int, movie int)  {
    
}


func (this *MovieRentingSystem) Report() [][]int {
    
}


/**
 * Your MovieRentingSystem object will be instantiated and called as such:
 * obj := Constructor(n, entries);
 * param_1 := obj.Search(movie);
 * obj.Rent(shop,movie);
 * obj.Drop(shop,movie);
 * param_4 := obj.Report();
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
	var entriesArr [][]int
	if v, ok := opValues[0][1].([][]int); ok {
		entriesArr = v
	} else {
		entriesArr = make([][]int, len(opValues[0][1].([]any)))
		for i := range entriesArr {
			entriesArr[i] = make([]int, len(opValues[0][1].([]any)[i].([]any)))
			for j := range entriesArr[i] {
				entriesArr[i][j] = int(opValues[0][1].([]any)[i].([]any)[j].(float64))
			}
		}
	}
	obj := Constructor(int(opValues[0][0].(float64)), entriesArr)
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res any
		switch operators[i] {
		case "search", "Search":
			res = obj.Search(int(opValues[i][0].(float64)))
		case "rent", "Rent":
			res = nil
			obj.Rent(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		case "drop", "Drop":
			res = nil
			obj.Drop(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		case "report", "Report":
			res = obj.Report()
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
