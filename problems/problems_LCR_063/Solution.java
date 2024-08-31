package problems.problems_LCR_063;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String replaceWords(List<String> dictionary, String sentence) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        List<String> dictionary = jsonArrayToStringList(inputJsonValues[0]);
		String sentence = jsonStringToString(inputJsonValues[1]);
        return JSON.toJSON(replaceWords(dictionary, sentence));
    }
}
