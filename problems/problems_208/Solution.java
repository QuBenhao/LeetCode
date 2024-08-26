package problems.problems_208;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class Trie {

    public Trie() {

    }
    
    public void insert(String word) {

    }
    
    public boolean search(String word) {

    }
    
    public boolean startsWith(String prefix) {

    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */

public class Solution extends BaseSolution {


    @Override
    public Object solve(String[] inputJsonValues) {
        String[] operators = jsonArrayToStringArray(inputJsonValues[0]);
		String[][] opValues = jsonArrayToString2DArray(inputJsonValues[1]);
		
		Trie obj = new Trie();
		List<Object> ans = new ArrayList<>(operators.length);
		ans.add(null);
		for (int i = 1; i < operators.length; i++) {
			if (operators[i].compareTo("insert") == 0) {
				String word = jsonStringToString(opValues[i][0]);
				obj.insert(word);
				ans.add(null);
				continue;
			}
			if (operators[i].compareTo("search") == 0) {
				String word = jsonStringToString(opValues[i][0]);
				ans.add(obj.search(word));
				continue;
			}
			if (operators[i].compareTo("startsWith") == 0) {
				String prefix = jsonStringToString(opValues[i][0]);
				ans.add(obj.startsWith(prefix));
				continue;
			}
			ans.add(null);
		}
        return JSON.toJSON(ans);
    }
}
