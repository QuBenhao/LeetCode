# 3171. 找到按位或最接近 K 的子数组 [难度分: 2162.69]

<p>给你一个数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code>&nbsp;。你需要找到&nbsp;<code>nums</code>&nbsp;的一个&nbsp;<span data-keyword="subarray-nonempty">子数组</span>&nbsp;，满足子数组中所有元素按位或运算 <code>OR</code> 的值与 <code>k</code>&nbsp;的 <strong>绝对差</strong>&nbsp;尽可能 <strong>小</strong>&nbsp;。换言之，你需要选择一个子数组&nbsp;<code>nums[l..r]</code>&nbsp;满足 <code>|k - (nums[l] OR nums[l + 1] ... OR nums[r])|</code>&nbsp;最小。</p>

<p>请你返回 <strong>最小</strong>&nbsp;的绝对差值。</p>

<p><strong>子数组 </strong>是数组中连续的&nbsp;<strong>非空</strong>&nbsp;元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,4,5], k = 3</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>

<p><strong>解释：</strong></p>

<p>子数组&nbsp;<code>nums[0..1]</code> 的按位 <code>OR</code> 运算值为 3 ，得到最小差值&nbsp;<code>|3 - 3| = 0</code> 。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,3,1,3], k = 2</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><strong>解释：</strong></p>

<p>子数组&nbsp;<code>nums[1..1]</code> 的按位 <code>OR</code> 运算值为 3 ，得到最小差值&nbsp;<code>|3 - 2| = 1</code> 。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1], k = 10</span></p>

<p><span class="example-io"><b>输出：</b>9</span></p>

<p><strong>解释：</strong></p>

<p>只有一个子数组，按位 <code>OR</code> 运算值为 1 ，得到最小差值&nbsp;<code>|10 - 1| = 9</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>
