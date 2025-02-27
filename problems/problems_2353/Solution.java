package problems.problems_2353;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class FoodRatings {

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        
    }
    
    public void changeRating(String food, int newRating) {
        
    }
    
    public String highestRated(String cuisine) {
        
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.changeRating(food,newRating);
 * String param_2 = obj.highestRated(cuisine);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		String[] foods = jsonArrayToStringArray(opValues[0][0]);
		String[] cuisines = jsonArrayToStringArray(opValues[0][1]);
		int[] ratings = jsonArrayToIntArray(opValues[0][2]);
		FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("changeRating") == 0) {
				String food = jsonStringToString(opValues[i][0]);
				int newRating = Integer.parseInt(opValues[i][1]);
				obj.changeRating(food, newRating);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("highestRated") == 0) {
				String cuisine = jsonStringToString(opValues[i][0]);
				ans.add(obj.highestRated(cuisine));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
