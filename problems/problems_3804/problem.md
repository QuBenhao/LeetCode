# 3804. Number of Centered Subarrays 

<p>You are given an integer array <code>nums</code>.</p>

<p>A <strong><span data-keyword="subarray-nonempty">subarray</span></strong> of <code>nums</code> is called <strong>centered</strong> if the sum of its elements is <strong>equal to at least one</strong> element within that <strong>same subarray</strong>.</p>

<p>Return the number of <strong>centered subarrays</strong> of <code>nums</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-1,1,0]</span></p>

<p><strong>Output:</strong> <span class="example-io">5</span></p>

<p><strong>Explanation:</strong></p>

<ul>
	<li>All single-element subarrays (<code>[-1]</code>, <code>[1]</code>, <code>[0]</code>) are centered.</li>
	<li>The subarray <code>[1, 0]</code> has a sum of 1, which is present in the subarray.</li>
	<li>The subarray <code>[-1, 1, 0]</code> has a sum of 0, which is present in the subarray.</li>
	<li>Thus, the answer is 5.</li>
</ul>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [2,-3]</span></p>

<p><strong>Output:</strong> <span class="example-io">2</span></p>

<p><strong>Explanation:</strong></p>

<p>Only single-element subarrays (<code>[2]</code>, <code>[-3]</code>) are centered.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 500</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
