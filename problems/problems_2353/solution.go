package problem2353

import (
	"encoding/json"
	"log"
	"strings"
)

type FoodRatings struct {
    
}


func Constructor(foods []string, cuisines []string, ratings []int) FoodRatings {
    
}


func (this *FoodRatings) ChangeRating(food string, newRating int)  {
    
}


func (this *FoodRatings) HighestRated(cuisine string) string {
    
}


/**
 * Your FoodRatings object will be instantiated and called as such:
 * obj := Constructor(foods, cuisines, ratings);
 * obj.ChangeRating(food,newRating);
 * param_2 := obj.HighestRated(cuisine);
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
	var arr []int
	if v, ok := opValues[0][2].([]int); ok {
		arr = v
	} else {
		for _, vi := range opValues[0][2].([]interface{}) {
			arr = append(arr, int(vi.(float64)))
		}
	}
	obj := Constructor(arr, arr, arr)
	ans = append(ans, nil)
	for i := 1; i < len(operators); i++ {
		var res interface{}
		switch operators[i] {
		case "changeRating", "ChangeRating":
			res = nil
			obj.ChangeRating(opValues[i][0].(string), int(opValues[i][1].(float64)))
		case "highestRated", "HighestRated":
			res = obj.HighestRated(opValues[i][0].(string))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
