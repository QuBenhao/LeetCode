package problems.problems_3479;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numOfUnplacedFruits(int[] fruits, int[] baskets) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] fruits = jsonArrayToIntArray(inputJsonValues[0]);
		int[] baskets = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(numOfUnplacedFruits(fruits, baskets));
    }
}
