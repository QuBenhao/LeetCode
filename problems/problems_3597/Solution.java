package problems.problems_3597;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {

    private class TrieNode {
        Map<Character, TrieNode> children;
        boolean isEndOfWord;

        TrieNode() {
            children = new HashMap<>();
            isEndOfWord = false;
        }

        int searchAndInsert(String word, int start) {
            int n = word.length();
            TrieNode node = this;
            for (int i = start; i < n; ++i) {
                char c = word.charAt(i);
                if (!node.children.containsKey(c)) {
                    TrieNode newNode = new TrieNode();
                    node.children.put(c, newNode);
                    newNode.isEndOfWord = true;
                    return i + 1;
                }
                node = node.children.get(c);
            }
            if (node.isEndOfWord) {
                return -1;
            }
            return n;
        }
    }

    public List<String> partitionString(String s) {
        TrieNode root = new TrieNode();
        List<String> result = new ArrayList<>();
        for (int i = 0, n = s.length(); i < n; ) {
            int nextIndex = root.searchAndInsert(s, i);
            if (nextIndex == -1) {
                break;
            }
            result.add(s.substring(i, nextIndex));
            i = nextIndex;
        }
        return  result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String s = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(partitionString(s));
    }
}
