package problem3815

import (
	"encoding/json"
	"log"
	"strings"
)

type AuctionSystem struct {
    
}


func Constructor() AuctionSystem {
    
}


func (this *AuctionSystem) AddBid(userId int, itemId int, bidAmount int)  {
    
}


func (this *AuctionSystem) UpdateBid(userId int, itemId int, newAmount int)  {
    
}


func (this *AuctionSystem) RemoveBid(userId int, itemId int)  {
    
}


func (this *AuctionSystem) GetHighestBidder(itemId int) int {
    
}


/**
 * Your AuctionSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddBid(userId,itemId,bidAmount);
 * obj.UpdateBid(userId,itemId,newAmount);
 * obj.RemoveBid(userId,itemId);
 * param_4 := obj.GetHighestBidder(itemId);
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
		case "addBid", "AddBid":
			res = nil
			obj.AddBid(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)), int(opValues[i][2].(float64)))
		case "updateBid", "UpdateBid":
			res = nil
			obj.UpdateBid(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)), int(opValues[i][2].(float64)))
		case "removeBid", "RemoveBid":
			res = nil
			obj.RemoveBid(int(opValues[i][0].(float64)), int(opValues[i][1].(float64)))
		case "getHighestBidder", "GetHighestBidder":
			res = obj.GetHighestBidder(int(opValues[i][0].(float64)))
		default:
			res = nil
		}
		ans = append(ans, res)
	}


	return ans
}
