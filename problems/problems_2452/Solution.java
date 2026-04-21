package problems.problems_2452;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public List<String> twoEditWords(String[] queries, String[] dictionary) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] queries = jsonArrayToStringArray(inputJsonValues[0]);
		String[] dictionary = jsonArrayToStringArray(inputJsonValues[1]);
        return JSON.toJSON(twoEditWords(queries, dictionary));
    }
}
