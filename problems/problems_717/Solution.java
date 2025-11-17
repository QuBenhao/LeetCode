package problems.problems_717;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isOneBitCharacter(int[] bits) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] bits = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(isOneBitCharacter(bits));
    }
}
