# [Rust] 二分

> Author: Benhao
> Date: 2024-09-04
> Upvotes: 1
> Tags: Rust

---


> Problem: [4. 寻找两个正序数组的中位数](https://leetcode.cn/problems/median-of-two-sorted-arrays/description/)

# Code
```Rust []
impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
		let m = nums1.len();
		let n = nums2.len();
		if m > n {
			return Solution::find_median_sorted_arrays(nums2, nums1);
		}
		let half_len = (m + n + 1) / 2;
		let mut left = 0;
		let mut right = m;
		while left < right {
			let i = left + (right - left) / 2;
			let j = half_len - i;
			if nums2[j - 1] > nums1[i] {
				left = i + 1;
			} else {
				right = i;
			}
		}
		let i = left;
		let j = half_len - i;
		let nums1_left_max = if i == 0 { i32::MIN } else { nums1[i - 1] };
		let nums1_right_min = if i == m { i32::MAX } else { nums1[i] };
		let nums2_left_max = if j == 0 { i32::MIN } else { nums2[j - 1] };
		let nums2_right_min = if j == n { i32::MAX } else { nums2[j] };
		if (m + n) % 2 == 1 {
			nums1_left_max.max(nums2_left_max) as f64
		} else {
			(nums1_left_max.max(nums2_left_max) + nums1_right_min.min(nums2_right_min)) as f64 / 2.0
		}
    }
}
```
  
