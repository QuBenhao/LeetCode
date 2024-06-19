package problems.problems_422;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean validWordSquare(List<String> words) {

    }

    @Override
    public Object solve(String[] values) {
        List<String> words = jsonArrayToStringList(values[0]);
        return JSON.toJSON(validWordSquare(words));
    }
}
