package problems.problems_3274;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean checkTwoChessboards(String coordinate1, String coordinate2) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String coordinate1 = jsonStringToString(inputJsonValues[0]);
		String coordinate2 = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(checkTwoChessboards(coordinate1, coordinate2));
    }
}
