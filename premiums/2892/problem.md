# 2892. Minimizing Array After Replacing Pairs With Their Product

<p>Given an integer array <code>nums</code> and an integer <code>k</code>, you can perform the following operation on the array any number of times:</p>

<ul>
	<li>Select two <strong>adjacent</strong> elements of the array like <code>x</code> and <code>y</code>, such that <code>x * y &lt;= k</code>, and replace both of them with a <strong>single element</strong> with value <code>x * y</code> (e.g. in one operation the array <code>[1, 2, 2, 3]</code> with <code>k = 5</code> can become <code>[1, 4, 3]</code> or <code>[2, 2, 3]</code>, but can&#39;t become <code>[1, 2, 6]</code>).</li>
</ul>

<p>Return <em>the <strong>minimum</strong> possible length of </em><code>nums</code><em> after any number of operations</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3,3,7,3,5], k = 20
<strong>Output:</strong> 3
<strong>Explanation:</strong> We perform these operations:
1. [<u>2,3</u>,3,7,3,5] -&gt; [<u>6</u>,3,7,3,5]
2. [<u>6,3</u>,7,3,5] -&gt; [<u>18</u>,7,3,5]
3. [18,7,<u>3,5</u>] -&gt; [18,7,<u>15</u>]
It can be shown that 3 is the minimum length possible to achieve with the given operation.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [3,3,3,3], k = 6
<strong>Output:</strong> 4
<strong>Explanation:</strong> We can&#39;t perform any operations since the product of every two adjacent elements is greater than 6.
Hence, the answer is 4.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>
