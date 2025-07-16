package problems.problems_658;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int binarySearch(int[] arr, int x) {
        int left = 0, right = arr.length - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] < x) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> result = new ArrayList<>(k);
        int right = binarySearch(arr, x);
        int left = right - 1;
        int n = arr.length;
        x <<= 1;
        while (k > 0 && left >= 0 && right < n) {
            if (arr[left] + arr[right] >= x) {
                --left;
            } else {
                ++right;
            }
            --k;
        }
        if (k > 0) {
            if (right == n) {
                left -= k;
            } else {
                right += k;
            }
        }
        for (int i = left + 1; i < right; ++i) {
            result.add(arr[i]);
        }
        return result;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] arr = jsonArrayToIntArray(inputJsonValues[0]);
		int k = Integer.parseInt(inputJsonValues[1]);
		int x = Integer.parseInt(inputJsonValues[2]);
        return JSON.toJSON(findClosestElements(arr, k, x));
    }
}
