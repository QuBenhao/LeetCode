package problems.problems_3838;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String mapWordWeights(String[] words, int[] weights) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
		int[] weights = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(mapWordWeights(words, weights));
    }
}
