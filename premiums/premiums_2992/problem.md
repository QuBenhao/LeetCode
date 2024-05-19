# 2992. Number of Self-Divisible Permutations

<p>Given an integer <code>n</code>, return <em>the number of <strong>permutations</strong> of the <strong>1-indexed</strong> array</em> <code>nums = [1, 2, ..., n]</code><em>, such that it&#39;s <strong>self-divisible</strong></em>.</p>

<p>A <strong>1-indexed</strong> array <code>a</code> of length <code>n</code> is <strong>self-divisible</strong> if for every <code>1 &lt;= i &lt;= n</code>, <code><span data-keyword="gcd-function">gcd</span>(a[i], i) == 1</code>.</p>

<p>A <strong>permutation</strong> of an array is a rearrangement of the elements of that array, for example here are all of the permutations of the array <code>[1, 2, 3]</code>:</p>

<ul>
	<li><code>[1, 2, 3]</code></li>
	<li><code>[1, 3, 2]</code></li>
	<li><code>[2, 1, 3]</code></li>
	<li><code>[2, 3, 1]</code></li>
	<li><code>[3, 1, 2]</code></li>
	<li><code>[3, 2, 1]</code></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> The array [1] has only 1 permutation which is self-divisible.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2
<strong>Output:</strong> 1
<strong>Explanation:</strong> The array [1,2] has 2 permutations and only one of them is self-divisible:
nums = [1,2]: This is not self-divisible since gcd(nums[2], 2) != 1.
nums = [2,1]: This is self-divisible since gcd(nums[1], 1) == 1 and gcd(nums[2], 2) == 1.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> The array [1,2,3] has 3 self-divisble permutations: [1,3,2], [3,1,2], [2,3,1].
It can be shown that the other 3 permutations are not self-divisible. Hence the answer is 3.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 12</code></li>
</ul>
