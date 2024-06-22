package problem1603

import (
	"encoding/json"
	"log"
	"strings"
)

type ParkingSystem struct {

}


func Constructor(big int, medium int, small int) ParkingSystem {

}


func (this *ParkingSystem) AddCar(carType int) bool {

}


/**
 * Your ParkingSystem object will be instantiated and called as such:
 * obj := Constructor(big, medium, small);
 * param_1 := obj.AddCar(carType);
 */

func Solve(input string) interface{} {
	values := strings.Split(input, "\n")
	var opts []string
	var vals [][]interface{}
	var ans []interface{}
	if err := json.Unmarshal([]byte(values[0]), &opts); err != nil {
		log.Println(err)
		return nil
	}
	if err := json.Unmarshal([]byte(values[1]), &vals); err != nil {
		log.Println(err)
		return nil
	}
	obj :=Constructor(int(vals[0][0].(float64)), int(vals[0][1].(float64)), int(vals[0][2].(float64)))
	ans = append(ans, nil)
	for i := 1; i < len(opts); i++ {
		var res interface{}
		switch opts[i] {
		case "addCar", "AddCar":
			res = obj.AddCar(int(vals[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
