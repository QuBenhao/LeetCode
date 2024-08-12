package problems.problems_676;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


class TrieNode {
	Map<Character, TrieNode> children;
	boolean isEnd;
	public TrieNode() {
		children = new HashMap<>();
		isEnd = false;
	}

	void addWord(String word) {
		TrieNode node = this;
		for (char c : word.toCharArray()) {
			if (!node.children.containsKey(c)) {
				node.children.put(c, new TrieNode());
			}
			node = node.children.get(c);
		}
		node.isEnd = true;
	}

	static boolean query(TrieNode node, String word, int idx, int remain) {
		if (idx == word.length()) {
			return node.isEnd && remain == 0;
		}
		char c = word.charAt(idx);
		if (node.children.containsKey(c)) {
			if (query(node.children.get(c), word, idx + 1, remain)) {
				return true;
			}
		}
		if (remain-- == 0) {
			return false;
		}
		for (char nxt: node.children.keySet()) {
			if (nxt == c) {
				continue;
			}
			if (query(node.children.get(nxt), word, idx + 1, remain)) {
				return true;
			}
		}
		return false;
	}
}

class MagicDictionary {
	private final TrieNode root;
    public MagicDictionary() {
		root = new TrieNode();
    }
    
    public void buildDict(String[] dictionary) {
		for (String word: dictionary) {
			root.addWord(word);
		}
    }
    
    public boolean search(String searchWord) {
		return TrieNode.query(root, searchWord, 0, 1);
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
