package problems.problems_3582;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String generateTag(String caption) {
        StringBuilder sb = new StringBuilder("#");
        String[] words = caption.split(" ");
        boolean first = true;
        for (String word : words) {
            if (word.isBlank()) continue;
            if (first) {
                for (int i = 0; i < word.length(); i++) {
                    sb.append(Character.toLowerCase(word.charAt(i)));
                }
                first = false;
            } else {
                sb.append(Character.toUpperCase(word.charAt(0)));
                for (int i = 1; i < word.length(); i++) {
                    sb.append(Character.toLowerCase(word.charAt(i)));
                }
            }
        }
        return sb.length() > 100 ? sb.substring(0, 100) : sb.toString();
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String caption = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(generateTag(caption));
    }
}
