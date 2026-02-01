package problem3829

import (
	"encoding/json"
	"log"
	"strings"
)

type RideSharingSystem struct {
    
}


func Constructor() RideSharingSystem {
    
}


func (this *RideSharingSystem) AddRider(riderId int)  {
    
}


func (this *RideSharingSystem) AddDriver(driverId int)  {
    
}


func (this *RideSharingSystem) MatchDriverWithRider() []int {
    
}


func (this *RideSharingSystem) CancelRider(riderId int)  {
    
}


/**
 * Your RideSharingSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddRider(riderId);
 * obj.AddDriver(driverId);
 * param_3 := obj.MatchDriverWithRider();
 * obj.CancelRider(riderId);
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
		case "addRider", "AddRider":
			res = nil
			obj.AddRider(int(opValues[i][0].(float64)))
		case "addDriver", "AddDriver":
			res = nil
			obj.AddDriver(int(opValues[i][0].(float64)))
		case "matchDriverWithRider", "MatchDriverWithRider":
			res = obj.MatchDriverWithRider()
		case "cancelRider", "CancelRider":
			res = nil
			obj.CancelRider(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
