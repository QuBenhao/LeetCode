package problems.problems_1550;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean threeConsecutiveOdds(int[] arr) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(threeConsecutiveOdds(arr));
    }
}
