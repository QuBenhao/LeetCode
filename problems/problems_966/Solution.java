package problems.problems_966;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String[] spellchecker(String[] wordlist, String[] queries) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] wordlist = jsonArrayToStringArray(inputJsonValues[0]);
		String[] queries = jsonArrayToStringArray(inputJsonValues[1]);
        return JSON.toJSON(spellchecker(wordlist, queries));
    }
}
