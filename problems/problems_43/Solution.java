package problems.problems_43;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String multiply(String num1, String num2) {

    }

    @Override
    public Object solve(String[] values) {
        String num1 = values[0];
		String num2 = values[1];
        return JSON.toJSON(multiply(num1, num2));
    }
}
