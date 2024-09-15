package problems.problems_LCR_064;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;

class TrieNode {
	TrieNode[] children;
	boolean isEnd;

	public TrieNode() {
		children = new TrieNode[26];
		isEnd = false;
	}

	public static boolean query(TrieNode root, String word, int index, int count, boolean change) {
		if (index == word.length()) {
			return count == 1 && root.isEnd;
		}
		char ch = word.charAt(index);
		if (!change) {
			for (int i = 0; i < 26; i++) {
				if (i == ch - 'a') {
					continue;
				}
				if (root.children[i] != null && query(root.children[i], word, index + 1, count + 1, true)) {
					return true;
				}
			}
		}
		return root.children[ch - 'a'] != null && query(root.children[ch - 'a'], word, index + 1, count, change);
	}
}


class MagicDictionary {
	private final TrieNode root;

    /** Initialize your data structure here. */
    public MagicDictionary() {
		root = new TrieNode();
    }
    
    public void buildDict(String[] dictionary) {
		for (String word : dictionary) {
			TrieNode cur = root;
			for (char ch : word.toCharArray()) {
				if (cur.children[ch - 'a'] == null) {
					cur.children[ch - 'a'] = new TrieNode();
				}
				cur = cur.children[ch - 'a'];
			}
			cur.isEnd = true;
		}
    }
    
    public boolean search(String searchWord) {
		return TrieNode.query(root, searchWord, 0, 0, false);
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
