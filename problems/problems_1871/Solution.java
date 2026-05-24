package problems.problems_1871;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean canReach(String s, int minJump, int maxJump) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
		int minJump = Integer.parseInt(inputJsonValues[1]);
		int maxJump = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(canReach(s, minJump, maxJump));
    }
}
