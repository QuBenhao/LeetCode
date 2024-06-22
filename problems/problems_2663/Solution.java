package problems.problems_2663;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String smallestBeautifulString(String S, int k) {
        k += 'a';
        char[] s = S.toCharArray();
        int n = s.length;
        int i = n - 1; // 从最后一个字母开始
        s[i]++; // 先加一
        while (i < n) {
            if (s[i] == k) { // 需要进位
                if (i == 0) { // 无法进位
                    return "";
                }
                // 进位
                s[i] = 'a';
                s[--i]++;
            } else if (i > 0 && s[i] == s[i - 1] || i > 1 && s[i] == s[i - 2]) {
                s[i]++; // 如果 s[i] 和左侧的字符形成回文串，就继续增加 s[i]
            } else {
                i++; // 反过来检查后面是否有回文串
            }
        }
        return new String(s);
    }

    @Override
    public Object solve(String[] values) {
        String s = jsonStringToString(values[0]);
		int k = Integer.parseInt(values[1]);
        return JSON.toJSON(smallestBeautifulString(s, k));
    }
}
