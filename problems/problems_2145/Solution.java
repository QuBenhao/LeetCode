package problems.problems_2145;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfArrays(int[] differences, int lower, int upper) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] differences = jsonArrayToIntArray(inputJsonValues[0]);
		int lower = Integer.parseInt(inputJsonValues[1]);
		int upper = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(numberOfArrays(differences, lower, upper));
    }
}
