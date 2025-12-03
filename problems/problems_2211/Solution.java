package problems.problems_2211;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int countCollisions(String directions) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String directions = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(countCollisions(directions));
    }
}
