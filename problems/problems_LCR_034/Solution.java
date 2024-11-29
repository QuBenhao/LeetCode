package problems.problems_LCR_034;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean isAlienSorted(String[] words, String order) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] words = jsonArrayToStringArray(inputJsonValues[0]);
		String order = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(isAlienSorted(words, order));
    }
}
