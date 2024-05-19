# 2436. Minimum Split Into Subarrays With GCD Greater Than One

<p>You are given an array <code>nums</code> consisting of positive integers.</p>

<p>Split the array into <strong>one or more</strong> disjoint subarrays such that:</p>

<ul>
	<li>Each element of the array belongs to <strong>exactly one</strong> subarray, and</li>
	<li>The <strong>GCD</strong> of the elements of each subarray is strictly greater than <code>1</code>.</li>
</ul>

<p>Return <em>the minimum number of subarrays that can be obtained after the split</em>.</p>

<p><strong>Note</strong> that:</p>

<ul>
	<li>The <strong>GCD</strong> of a subarray is the largest positive integer that evenly divides all the elements of the subarray.</li>
	<li>A <strong>subarray</strong> is a contiguous part of the array.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [12,6,3,14,8]
<strong>Output:</strong> 2
<strong>Explanation:</strong> We can split the array into the subarrays: [12,6,3] and [14,8].
- The GCD of 12, 6 and 3 is 3, which is strictly greater than 1.
- The GCD of 14 and 8 is 2, which is strictly greater than 1.
It can be shown that splitting the array into one subarray will make the GCD = 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,12,6,14]
<strong>Output:</strong> 1
<strong>Explanation:</strong> We can split the array into only one subarray, which is the whole array.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2000</code></li>
	<li><code>2 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
