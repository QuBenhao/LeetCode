package problems.problems_638;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int shoppingOffers(List<Integer> price, List<List<Integer>> special, List<Integer> needs) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<Integer> price = jsonArrayToIntList(inputJsonValues[0]);
		List<List<Integer>> special = jsonArrayTo2DIntList(inputJsonValues[1]);
		List<Integer> needs = jsonArrayToIntList(inputJsonValues[2]);
        return JSON.toJSON(shoppingOffers(price, special, needs));
    }
}
