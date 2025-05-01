package problems.problems_838;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String pushDominoes(String dominoes) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String dominoes = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(pushDominoes(dominoes));
    }
}
