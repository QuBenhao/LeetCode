package problems.problems_3129;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int numberOfStableArrays(int zero, int one, int limit) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int zero = Integer.parseInt(inputJsonValues[0]);
		int one = Integer.parseInt(inputJsonValues[1]);
		int limit = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(numberOfStableArrays(zero, one, limit));
    }
}
