package problems.problems_679;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean judgePoint24(int[] cards) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] cards = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(judgePoint24(cards));
    }
}
