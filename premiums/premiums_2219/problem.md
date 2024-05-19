# 2219. Maximum Sum Score of Array

<p>You are given a <strong>0-indexed</strong> integer array <code>nums</code> of length <code>n</code>.</p>

<p>The <strong>sum </strong><strong>score</strong> of <code>nums</code> at an index <code>i</code> where <code>0 &lt;= i &lt; n</code> is the <strong>maximum</strong> of:</p>

<ul>
	<li>The sum of the <strong>first</strong> <code>i + 1</code> elements of <code>nums</code>.</li>
	<li>The sum of the <strong>last</strong> <code>n - i</code> elements of <code>nums</code>.</li>
</ul>

<p>Return <em>the <strong>maximum</strong> <strong>sum </strong><strong>score</strong> of </em><code>nums</code><em> at any index.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,3,-2,5]
<strong>Output:</strong> 10
<strong>Explanation:</strong>
The sum score at index 0 is max(4, 4 + 3 + -2 + 5) = max(4, 10) = 10.
The sum score at index 1 is max(4 + 3, 3 + -2 + 5) = max(7, 6) = 7.
The sum score at index 2 is max(4 + 3 + -2, -2 + 5) = max(5, 3) = 5.
The sum score at index 3 is max(4 + 3 + -2 + 5, 5) = max(10, 5) = 10.
The maximum sum score of nums is 10.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [-3,-5]
<strong>Output:</strong> -3
<strong>Explanation:</strong>
The sum score at index 0 is max(-3, -3 + -5) = max(-3, -8) = -3.
The sum score at index 1 is max(-3 + -5, -5) = max(-8, -5) = -5.
The maximum sum score of nums is -3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
