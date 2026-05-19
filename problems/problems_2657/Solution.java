package problems.problems_2657;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] A = jsonArrayToIntArray(inputJsonValues[0]);
		int[] B = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(findThePrefixCommonArray(A, B));
    }
}
