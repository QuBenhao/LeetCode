package problems.problems_2040;

import com.alibaba.fastjson.JSON;
import java.util.*;
import qubhjava.BaseSolution;


public class Solution extends BaseSolution {
    private int bisectLeft(int[] nums, int target) {
        int left = 0, right = nums.length;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    private boolean check(int[] nums1, int[] nums2, long x, long k, int zero1, int zero2) {
        long count;
        int m = nums1.length, n = nums2.length;
        if (x < 0) {
            count = 0;
            int i = 0, j = zero2;
            while (i < zero1 && j < n) {
                if ((long)nums1[i] * nums2[j] > x) {
                    ++j;
                } else {
                    count += n - j;
                    ++i;
                }
            }
            i = zero1; j = 0;
            while (i < m && j < zero2) {
                if ((long)nums1[i] * nums2[j] > x) {
                    ++i;
                } else {
                    count += m - i;
                    ++j;
                }
            }
        } else {
            count = (long)zero1 * (n - zero2) + (long)(m - zero1) * zero2;
            int i = 0, j = zero2 - 1;
            while (i < zero1 && j >= 0) {
                if ((long)nums1[i] * nums2[j] > x) {
                    ++i;
                } else {
                    count += zero1 - i;
                    --j;
                }
            }
            i = zero1; j = n - 1;
            while (i < m && j >= zero2) {
                if ((long)nums1[i] * nums2[j] > x) {
                    --j;
                } else {
                    count += j - zero2 + 1;
                    ++i;
                }
            }
        }
        return count >= k;
    }

    public long kthSmallestProduct(int[] nums1, int[] nums2, long k) {
        int zero1 = bisectLeft(nums1, 0), zero2 = bisectLeft(nums2, 0);
        int m = nums1.length, n = nums2.length;
        List<Long> corners = Arrays.asList((long)nums1[0] * nums2[0],
                                           (long)nums1[0] * nums2[n - 1],
                                           (long)nums1[m - 1] * nums2[0],
                                           (long)nums1[m - 1] * nums2[n - 1]);
        long left = Collections.min(corners), right = Collections.max(corners);
        while (left < right) {
            long mid = left + (right - left) / 2;
            if (check(nums1, nums2, mid, k, zero1, zero2)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    @Override
    public Object solve(String[] inputJsonValues) {
        int[] nums1 = jsonArrayToIntArray(inputJsonValues[0]);
		int[] nums2 = jsonArrayToIntArray(inputJsonValues[1]);
		long k = Long.parseLong(inputJsonValues[2]);
        return JSON.toJSON(kthSmallestProduct(nums1, nums2, k));
    }
}
