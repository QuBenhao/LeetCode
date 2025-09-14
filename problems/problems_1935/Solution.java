package problems.problems_1935;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int canBeTypedWords(String text, String brokenLetters) {
        int brokenMask = 0;
        for (char c : brokenLetters.toCharArray()) {
            brokenMask |= 1 << (c - 'a'); // 把 c 加到集合中
        }

        int ans = 0;
        int ok = 1;
        for (char c : text.toCharArray()) {
            if (c == ' ') { // 上一个单词遍历完毕
                ans += ok;
                ok = 1;
            } else if ((brokenMask >> (c - 'a') & 1) > 0) { // c 在 brokenLetters 中
                ok = 0;
            }
        }
        ans += ok; // 最后一个单词
        return ans;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String text = jsonStringToString(inputJsonValues[0]);
		String brokenLetters = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(canBeTypedWords(text, brokenLetters));
    }
}
