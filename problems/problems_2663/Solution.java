package problems.problems_2663;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String smallestBeautifulString(String s, int k) {

    }

    @Override
    public Object solve(String[] values) {
        String s = jsonStringToString(values[0]);
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(smallestBeautifulString(s, k));
    }
}
