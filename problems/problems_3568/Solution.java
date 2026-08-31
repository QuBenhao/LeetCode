package problems.problems_3568;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int minMoves(String[] classroom, int energy) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] classroom = jsonArrayToStringArray(inputJsonValues[0]);
		int energy = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(minMoves(classroom, energy));
    }
}
