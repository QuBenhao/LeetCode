package problems.problems_422;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean validWordSquare(List<String> words) {
        for (int i = 0; i < words.size(); i++) {
            String word = words.get(i);
            if (word.length() > words.size()) {
                return false;
            }
            for (int j = 0; j < i; j++) {
                if ((word.length() <= j) != (words.get(j).length() <= i)) {
                    return false;
                } else if (word.length() > j && word.charAt(j) != words.get(j).charAt(i)) {
                    return false;
                }
            }
        }
        return true;
    }

    @Override
    public Object solve(String[] values) {
        List<String> words = jsonArrayToStringList(values[0]);
        return JSON.toJSON(validWordSquare(words));
    }
}
