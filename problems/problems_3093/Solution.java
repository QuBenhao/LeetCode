package problems.problems_3093;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] stringIndices(String[] wordsContainer, String[] wordsQuery) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] wordsContainer = jsonArrayToStringArray(inputJsonValues[0]);
		String[] wordsQuery = jsonArrayToStringArray(inputJsonValues[1]);
        return JSON.toJSON(stringIndices(wordsContainer, wordsQuery));
    }
}
