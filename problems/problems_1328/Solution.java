package problems.problems_1328;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public String breakPalindrome(String palindrome) {
        
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String palindrome = jsonStringToString(inputJsonValues[0]);
        return JSON.toJSON(breakPalindrome(palindrome));
    }
}
