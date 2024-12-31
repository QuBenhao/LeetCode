package problems.problems_3280;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String convertDateToBinary(String date) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String date = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(convertDateToBinary(date));
    }
}
