package problems.problems_3403;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String answerString(String word, int numFriends) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String word = jsonStringToString(inputJsonValues[0]);
		int numFriends = Integer.parseInt(inputJsonValues[1]);
        return JSON.toJSON(answerString(word, numFriends));
    }
}
