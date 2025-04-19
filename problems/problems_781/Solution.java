package problems.problems_781;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numRabbits(int[] answers) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] answers = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(numRabbits(answers));
    }
}
