package problems.problems_LCR_062;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class Trie {

	private final Map<Character, Trie> children;
	private boolean isEnd;

    /** Initialize your data structure here. */
    public Trie() {
		this.children = new HashMap<>(26);
		this.isEnd = false;
    }
    
    /** Inserts a word into the trie. */
    public void insert(String word) {
		Trie node = this;
		for (char ch : word.toCharArray()) {
			if (!node.children.containsKey(ch)) {
				node.children.put(ch, new Trie());
			}
			node = node.children.get(ch);
		}
		node.isEnd = true;
    }

	private Trie searchPrefix(String prefix) {
		Trie node = this;
		for (char ch : prefix.toCharArray()) {
			if (!node.children.containsKey(ch)) {
				return null;
			}
			node = node.children.get(ch);
		}
		return node;
	}
    
    /** Returns if the word is in the trie. */
    public boolean search(String word) {
		Trie node = searchPrefix(word);
		return node != null && node.isEnd;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    public boolean startsWith(String prefix) {
		return searchPrefix(prefix) != null;
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
