package problems.problems_LCR_063;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private TrieNode root;
    class TrieNode {
        TrieNode[] children;
        boolean isEnd;

        public TrieNode() {
            children = new TrieNode[26];
            isEnd = false;
        }
    }

    private void insert(String word) {
        TrieNode node = root;
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                node.children[index] = new TrieNode();
            }
            node = node.children[index];
        }
        node.isEnd = true;
    }

    private String search(String word) {
        TrieNode node = root;
        StringBuilder sb = new StringBuilder();
        for (char c : word.toCharArray()) {
            int index = c - 'a';
            if (node.children[index] == null) {
                return word;
            }
            sb.append(c);
            node = node.children[index];
            if (node.isEnd) {
                return sb.toString();
            }
        }
        return word;
    }

    public String replaceWords(List<String> dictionary, String sentence) {
        root = new TrieNode();
        for (String word : dictionary) {
            insert(word);
        }
        String[] words = sentence.split(" ");
        StringBuilder sb = new StringBuilder();
        for (String word : words) {
            sb.append(search(word)).append(" ");
        }
        return sb.toString().trim();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<String> dictionary = jsonArrayToStringList(inputJsonValues[0]);
		String sentence = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(replaceWords(dictionary, sentence));
    }
}
