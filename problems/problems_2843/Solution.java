package problems.problems_2843;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countSymmetricIntegers(int low, int high) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int low = Integer.parseInt(inputJsonValues[0]);
		int high = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(countSymmetricIntegers(low, high));
    }
}
