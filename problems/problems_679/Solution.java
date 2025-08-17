package problems.problems_679;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private static final double TARGET = 24.0;
    private static final double EPSILON = 1e-6;

    private boolean backtack(List<Double> numbers) {
        if (numbers.size() == 1) {
            return Math.abs(numbers.get(0) - TARGET) < EPSILON;
        }

        for (int i = 0; i < numbers.size(); i++) {
            for (int j = i + 1; j < numbers.size(); j++) {
                if (i != j) {
                    List<Double> nextNumbers = new ArrayList<>();
                    for (int k = 0; k < numbers.size(); k++) {
                        if (k != i && k != j) {
                            nextNumbers.add(numbers.get(k));
                        }
                    }

                    double a = numbers.get(i);
                    double b = numbers.get(j);

                    // Try all operations
                    for (int op = 0; op < 6; ++op) {
                        switch (op) {
                            case 0: // a + b
                                nextNumbers.add(a + b);
                                break;
                            case 1: // a - b
                                nextNumbers.add(a - b);
                                break;
                            case 2: // b - a
                                nextNumbers.add(b - a);
                                break;
                            case 3: // a * b
                                nextNumbers.add(a * b);
                                break;
                            case 4: // a / b
                                if (Math.abs(b) < EPSILON) {
                                    continue; // Avoid division by zero
                                }
                                nextNumbers.add(a / b);
                                break;
                            case 5: // b / a
                                if (Math.abs(a) < EPSILON) {
                                    continue; // Avoid division by zero
                                }
                                nextNumbers.add(b / a);
                                break;
                        }
                        if (backtack(nextNumbers)) return true;
                        nextNumbers.remove(nextNumbers.size() - 1);
                    }
                }
            }
        }
        return false;
    }

    public boolean judgePoint24(int[] cards) {
        List<Double> numbers = new ArrayList<>();
        for (int card : cards) {
            numbers.add((double) card);
        }
        return backtack(numbers);
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] cards = jsonArrayToIntArray(inputJsonValues[0]);
        return JSON.toJSON(judgePoint24(cards));
    }
}
