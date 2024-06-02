package problems.problems_389;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public char findTheDifference(String s, String t) {

    }

    @Override
    public Object solve(String[] values) {
        String s = values[0];
		String t = values[1];
        return JSON.toJSON(findTheDifference(s, t));
    }
}
