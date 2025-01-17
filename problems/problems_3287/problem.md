# 3287. Find the Maximum Sequence Value of Array [Rating: 2545.11]

<p>You are given an integer array <code>nums</code> and a <strong>positive</strong> integer <code>k</code>.</p>

<p>The <strong>value</strong> of a sequence <code>seq</code> of size <code>2 * x</code> is defined as:</p>

<ul>
	<li><code>(seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1])</code>.</li>
</ul>

<p>Return the <strong>maximum</strong> <strong>value</strong> of any <span data-keyword="subsequence-array">subsequence</span> of <code>nums</code> having size <code>2 * k</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,6,7], k = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<p>The subsequence <code>[2, 7]</code> has the maximum value of <code>2 XOR 7 = 5</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,2,5,6,7], k = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>The subsequence <code>[4, 5, 6, 7]</code> has the maximum value of <code>(4 OR 5) XOR (6 OR 7) = 2</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 400</code></li>
	<li><code>1 &lt;= nums[i] &lt; 2<sup>7</sup></code></li>
	<li><code>1 &lt;= k &lt;= nums.length / 2</code></li>
</ul>
