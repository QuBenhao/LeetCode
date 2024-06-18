package problems.problems_2288;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String discountPrices(String sentence, int discount) {
        double d = (100.0 - discount) / 100.0;
        StringBuilder sb = new StringBuilder();
        out:
        for (String s: sentence.split(" ")) {
            if (s.length() > 1 && s.charAt(0) == '$') {
                long cur = 0L;
                for (int i = 1; i < s.length(); i++) {
                    if (s.charAt(i) < '0' || s.charAt(i) > '9') {
                        sb.append(s);
                        sb.append(' ');
                        continue out;
                    }
                    cur = 10 * cur + s.charAt(i) - '0';
                }
                sb.append(String.format("$%.2f", d * cur));
                sb.append(' ');
                continue;
            }
            sb.append(s);
            sb.append(' ');
        }
        return sb.substring(0, sb.length() - 1);
    }

    @Override
    public Object solve(String[] values) {
        String sentence = jsonStringToString(values[0]);
		int discount = Integer.parseInt(values[1]);
        return JSON.toJSON(discountPrices(sentence, discount));
    }
}
