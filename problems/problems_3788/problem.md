# 3788. Maximum Score of a Split 

<p>You are given an integer array <code>nums</code> of length <code>n</code>.</p>

<p>Choose an index <code>i</code> such that <code>0 &lt;= i &lt; n - 1</code>.</p>

<p>For a chosen split index <code>i</code>:</p>

<ul>
	<li>Let <code>prefixSum(i)</code> be the sum of <code>nums[0] + nums[1] + ... + nums[i]</code>.</li>
	<li>Let <code>suffixMin(i)</code> be the minimum value among <code>nums[i + 1], nums[i + 2], ..., nums[n - 1]</code>.</li>
</ul>

<p>The <strong>score</strong> of a split at index <code>i</code> is defined as:</p>

<p><code>score(i) = prefixSum(i) - suffixMin(i)</code></p>

<p>Return an integer denoting the <strong>maximum</strong> score over all valid split indices.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [10,-1,3,-4,-5]</span></p>

<p><strong>Output:</strong> <span class="example-io">17</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal split is at <code>i = 2</code>, <code>score(2) = prefixSum(2) - suffixMin(2) = (10 + (-1) + 3) - (-5) = 17</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [-7,-5,3]</span></p>

<p><strong>Output:</strong> <span class="example-io">-2</span></p>

<p><strong>Explanation:</strong></p>

<p>The optimal split is at <code>i = 0</code>, <code>score(0) = prefixSum(0) - suffixMin(0) = (-7) - (-5) = -2</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,1]</span></p>

<p><strong>Output:</strong> <span class="example-io">0</span></p>

<p><strong>Explanation:</strong></p>

<p>The only valid split is at <code>i = 0</code>, <code>score(0) = prefixSum(0) - suffixMin(0) = 1 - 1 = 0</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup>​​​​​​​ &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
