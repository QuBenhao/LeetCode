package problems.problems_2288;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String discountPrices(String sentence, int discount) {

    }

    @Override
    public Object solve(String[] values) {
        String sentence = jsonStringToString(values[0]);
		int discount = Integer.parseInt(values[1]);
        return JSON.toJSON(discountPrices(sentence, discount));
    }
}
