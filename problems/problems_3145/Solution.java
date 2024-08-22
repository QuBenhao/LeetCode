package problems.problems_3145;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    public int[] findProductsOfElements(long[][] queries) {

    }

    @Override
    public Object solve(String[] inputJsonValues) {
        long[][] queries = jsonArrayToLong2DArray(inputJsonValues[0]);
        return JSON.toJSON(findProductsOfElements(queries));
    }
}
