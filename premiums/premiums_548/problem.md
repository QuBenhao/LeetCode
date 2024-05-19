# 548. Split Array with Equal Sum

<p>Given an integer array <code>nums</code> of length <code>n</code>, return <code>true</code> if there is a triplet <code>(i, j, k)</code> which satisfies the following conditions:</p>

<ul>
	<li><code>0 &lt; i, i + 1 &lt; j, j + 1 &lt; k &lt; n - 1</code></li>
	<li>The sum of subarrays <code>(0, i - 1)</code>, <code>(i + 1, j - 1)</code>, <code>(j + 1, k - 1)</code> and <code>(k + 1, n - 1)</code> is equal.</li>
</ul>
A subarray <code>(l, r)</code> represents a slice of the original array starting from the element indexed <code>l</code> to the element indexed <code>r</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,2,1,2,1]
<strong>Output:</strong> true
<strong>Explanation:</strong>
i = 1, j = 3, k = 5. 
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [1,2,1,2,1,2,1,2]
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n ==&nbsp;nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 2000</code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>
