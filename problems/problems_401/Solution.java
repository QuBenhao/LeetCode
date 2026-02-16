package problems.problems_401;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<String> readBinaryWatch(int turnedOn) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int turnedOn = Integer.parseInt(inputJsonValues[0]);
        return JSON.toJSON(readBinaryWatch(turnedOn));
    }
}
