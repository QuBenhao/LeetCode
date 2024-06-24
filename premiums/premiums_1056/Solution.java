package premiums.premiums_1056;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public boolean confusingNumber(int n) {

    }

    @Override
    public Object solve(String[] values) {
        int n = Integer.parseInt(values[0]);
        return JSON.toJSON(confusingNumber(n));
    }
}
