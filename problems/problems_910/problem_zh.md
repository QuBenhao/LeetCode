# 910. 最小差值 II [难度分: 2134.54]

<p>给你一个整数数组 <code>nums</code>，和一个整数&nbsp;<code>k</code> 。</p>

<p>对于每个下标 <code>i</code>（<code>0 &lt;= i &lt; nums.length</code>），将 <code>nums[i]</code> 变成<strong> </strong> <code>nums[i] + k</code> 或 <code>nums[i] - k</code> 。</p>

<p><code>nums</code> 的 <strong>分数</strong> 是 <code>nums</code> 中最大元素和最小元素的差值。</p>

<p>在更改每个下标对应的值之后，返回 <code>nums</code> 的最小 <strong>分数</strong> 。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>nums = [1], k = 0
<strong>输出：</strong>0
<strong>解释：</strong>分数 = max(nums) - min(nums) = 1 - 1 = 0 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>nums = [0,10], k = 2
<strong>输出：</strong>6
<strong>解释：</strong>将数组变为 [2, 8] 。分数 = max(nums) - min(nums) = 8 - 2 = 6 。
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>nums = [1,3,6], k = 3
<strong>输出：</strong>3
<strong>解释：</strong>将数组变为 [4, 6, 3] 。分数 = max(nums) - min(nums) = 6 - 3 = 3 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>4</sup></code></li>
</ul>
