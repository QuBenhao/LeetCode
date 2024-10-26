package problems.problems_3181;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;
import java.math.BigInteger;

public class Solution extends BaseSolution {
    public int maxTotalReward(int[] rewardValues) {
        BigInteger f = BigInteger.ONE;
        for (int v : Arrays.stream(rewardValues).distinct().sorted().toArray()) {
            BigInteger mask = BigInteger.ONE.shiftLeft(v).subtract(BigInteger.ONE);
            f = f.or(f.and(mask).shiftLeft(v));
        }
        return f.bitLength() - 1;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] rewardValues = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(maxTotalReward(rewardValues));
    }
}
