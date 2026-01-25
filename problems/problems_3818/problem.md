# 3818. Minimum Prefix Removal to Make Array Strictly Increasing 

<p>You are given an integer array <code>nums</code>.</p>

<p>You need to remove <strong>exactly</strong> one prefix (possibly empty) from nums.</p>

<p>Return an integer denoting the <strong>minimum</strong> length of the removed prefix such that the remaining array is <strong>strictly increasing</strong>.</p>

<p>A <strong>prefix</strong> of an array is a subarray that starts from the beginning of the array and extends to any point within it.</p>

<p>An array is said to be <strong>strictly increasing</strong> if each element is strictly greater than its previous one (if exists).</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,-1,2,3,3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">4</span></p>

<p><strong>Explanation:</strong></p>

<p>Removing the <code>prefix = [1, -1, 2, 3]</code> leaves the remaining array <code>[3, 4, 5]</code> which is strictly increasing.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [4,3,-2,-5]</span></p>

<p><strong>Output:</strong> <span class="example-io">3</span></p>

<p><strong>Explanation:</strong></p>

<p>Removing the <code>prefix = [4, 3, -2]</code> leaves the remaining array <code>[-5]</code> which is strictly increasing.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The array <code>nums = [1, 2, 3, 4]</code> is already strictly increasing so removing an empty prefix is sufficient.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup>​​​​​​​</code></li>
</ul>
