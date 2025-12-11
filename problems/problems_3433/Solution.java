package problems.problems_3433;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] countMentions(int numberOfUsers, List<List<String>> events) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int numberOfUsers = Integer.parseInt(inputJsonValues[0]);
		List<List<String>> events = jsonArrayToString2DList(inputJsonValues[1]);
        return JSON.toJSON(countMentions(numberOfUsers, events));
    }
}
