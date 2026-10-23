package problems.problems_2409;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countDaysTogether(String arriveAlice, String leaveAlice, String arriveBob, String leaveBob) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String arriveAlice = jsonStringToString(inputJsonValues[0]);
		String leaveAlice = jsonStringToString(inputJsonValues[1]);
		String arriveBob = jsonStringToString(inputJsonValues[2]);
		String leaveBob = jsonStringToString(inputJsonValues[3]);
        return JSON.toJSON(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob));
    }
}
