package problems.problems_LCR_064;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class MagicDictionary {

    /** Initialize your data structure here. */
    public MagicDictionary() {

    }
    
    public void buildDict(String[] dictionary) {

    }
    
    public boolean search(String searchWord) {

    }
}

/**
 * Your MagicDictionary object will be instantiated and called as such:
 * MagicDictionary obj = new MagicDictionary();
 * obj.buildDict(dictionary);
 * boolean param_2 = obj.search(searchWord);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		MagicDictionary obj = new MagicDictionary();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("buildDict") == 0) {
				String[] dictionary = jsonArrayToStringArray(opValues[i][0]);
				obj.buildDict(dictionary);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("search") == 0) {
				String searchWord = jsonStringToString(opValues[i][0]);
				ans.add(obj.search(searchWord));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
