package problems.problems_LCR_108;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int ladderLength(String beginWord, String endWord, List<String> wordList) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String beginWord = jsonStringToString(inputJsonValues[0]);
		String endWord = jsonStringToString(inputJsonValues[1]);
		List<String> wordList = jsonArrayToStringList(inputJsonValues[2]);
        return JSON.toJSON(ladderLength(beginWord, endWord, wordList));
    }
}
