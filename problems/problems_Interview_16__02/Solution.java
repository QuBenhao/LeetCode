package problems.problems_Interview_16__02;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class WordsFrequency {

    public WordsFrequency(String[] book) {
        
    }
    
    public int get(String word) {
        
    }
}

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * WordsFrequency obj = new WordsFrequency(book);
 * int param_1 = obj.get(word);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		String[] book = jsonArrayToStringArray(opValues[0][0]);
		WordsFrequency obj = new WordsFrequency(book);
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("get") == 0) {
				String word = jsonStringToString(opValues[i][0]);
				ans.add(obj.get(word));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
