# 2964. Number of Divisible Triplet Sums

Given a <strong>0-indexed</strong> integer array <code>nums</code> and an integer <code>d</code>, return <em>the number of triplets</em> <code>(i, j, k)</code> <em>such that</em> <code>i &lt; j &lt; k</code> <em>and</em> <code>(nums[i] + nums[j] + nums[k]) % d == 0</code>.
<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,4,7,8], d = 5
<strong>Output:</strong> 3
<strong>Explanation:</strong> The triplets which are divisible by 5 are: (0, 1, 2), (0, 2, 4), (1, 2, 4).
It can be shown that no other triplet is divisible by 5. Hence, the answer is 3.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,3,3], d = 3
<strong>Output:</strong> 4
<strong>Explanation:</strong> Any triplet chosen here has a sum of 9, which is divisible by 3. Hence, the answer is the total number of triplets which is 4.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,3,3], d = 6
<strong>Output:</strong> 0
<strong>Explanation:</strong> Any triplet chosen here has a sum of 9, which is not divisible by 6. Hence, the answer is 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 1000</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= d &lt;= 10<sup>9</sup></code></li>
</ul>
