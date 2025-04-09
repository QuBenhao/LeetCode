package problems.problems_2999;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public long numberOfPowerfulInt(long start, long finish, int limit, String s) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long start = Long.parseLong(inputJsonValues[0]);
		long finish = Long.parseLong(inputJsonValues[1]);
		int limit = Integer.parseInt(inputJsonValues[2]);
		String s = jsonStringToString(inputJsonValues[3]);
        return JSON.toJSON(numberOfPowerfulInt(start, finish, limit, s));
    }
}
