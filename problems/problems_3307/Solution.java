package problems.problems_3307;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public char kthCharacter(long k, int[] operations) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long k = Long.parseLong(inputJsonValues[0]);
		int[] operations = jsonArrayToIntArray(inputJsonValues[1]);
        return JSON.toJSON(kthCharacter(k, operations));
    }
}
