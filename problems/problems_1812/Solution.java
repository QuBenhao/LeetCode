package problems.problems_1812;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean squareIsWhite(String coordinates) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String coordinates = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(squareIsWhite(coordinates));
    }
}
