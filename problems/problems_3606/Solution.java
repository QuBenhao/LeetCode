package problems.problems_3606;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final Map<String, Integer> BUSINESS_MAP = new HashMap<>() {
        {
            put("electronics", 0);
            put("grocery", 1);
            put("pharmacy", 2);
            put("restaurant", 3);
        }
    };

    public List<String> validateCoupons(String[] code, String[] businessLine, boolean[] isActive) {
        List<Integer> validIndices = new ArrayList<>();
        for (int i = 0; i < code.length; i++) {
            if (!isActive[i] || !BUSINESS_MAP.containsKey(businessLine[i])) { continue; }
            if (code[i].isEmpty()) { continue; }
            boolean valid = true;
            for (char c: code[i].toCharArray()) {
                if (!Character.isDigit(c) && !Character.isLetter(c) && c != '_') {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                validIndices.add(i);
            }
        }
        validIndices.sort((a, b) -> {
            int idxA = BUSINESS_MAP.get(businessLine[a]);
            int idxB = BUSINESS_MAP.get(businessLine[b]);
            if (idxA != idxB) {
                return Integer.compare(idxA, idxB);
            }
            return code[a].compareTo(code[b]);
        });
        List<String> result = new ArrayList<>();
        for (int idx : validIndices) {
            result.add(code[idx]);
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        String[] code = jsonArrayToStringArray(inputJsonValues[0]);
		String[] businessLine = jsonArrayToStringArray(inputJsonValues[1]);
		boolean[] isActive = jsonArrayToBooleanArray(inputJsonValues[2]);
        return JSON.toJSON(validateCoupons(code, businessLine, isActive));
    }
}
