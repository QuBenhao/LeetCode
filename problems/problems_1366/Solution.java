package problems.problems_1366;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String rankTeams(String[] votes) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] votes = jsonArrayToStringArray(inputJsonValues[0]);
        return JSON.toJSON(rankTeams(votes));
    }
}
