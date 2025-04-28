package problems.problems_344;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public void reverseString(char[] s) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        char[] s = jsonArrayToCharArray(inputJsonValues[0]);
		reverseString(s);
        return JSON.toJSON(s);
    }
}
