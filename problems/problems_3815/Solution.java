package problems.problems_3815;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class AuctionSystem {

    public AuctionSystem() {
        
    }
    
    public void addBid(int userId, int itemId, int bidAmount) {
        
    }
    
    public void updateBid(int userId, int itemId, int newAmount) {
        
    }
    
    public void removeBid(int userId, int itemId) {
        
    }
    
    public int getHighestBidder(int itemId) {
        
    }
}

/**
 * Your AuctionSystem object will be instantiated and called as such:
 * AuctionSystem obj = new AuctionSystem();
 * obj.addBid(userId,itemId,bidAmount);
 * obj.updateBid(userId,itemId,newAmount);
 * obj.removeBid(userId,itemId);
 * int param_4 = obj.getHighestBidder(itemId);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		AuctionSystem obj = new AuctionSystem();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("addBid") == 0) {
				int userId = Integer.parseInt(opValues[i][0]);
				int itemId = Integer.parseInt(opValues[i][1]);
				int bidAmount = Integer.parseInt(opValues[i][2]);
				obj.addBid(userId, itemId, bidAmount);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("updateBid") == 0) {
				int userId = Integer.parseInt(opValues[i][0]);
				int itemId = Integer.parseInt(opValues[i][1]);
				int newAmount = Integer.parseInt(opValues[i][2]);
				obj.updateBid(userId, itemId, newAmount);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("removeBid") == 0) {
				int userId = Integer.parseInt(opValues[i][0]);
				int itemId = Integer.parseInt(opValues[i][1]);
				obj.removeBid(userId, itemId);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("getHighestBidder") == 0) {
				int itemId = Integer.parseInt(opValues[i][0]);
				ans.add(obj.getHighestBidder(itemId));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
