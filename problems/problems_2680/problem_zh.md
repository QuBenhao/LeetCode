# 2680. 最大或值 [难度分: 1912.19]

<p>给你一个下标从 <strong>0</strong>&nbsp;开始长度为 <code>n</code>&nbsp;的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>k</code> 。每一次操作中，你可以选择一个数并将它乘&nbsp;<code>2</code>&nbsp;。</p>

<p>你最多可以进行 <code>k</code>&nbsp;次操作，请你返回<em>&nbsp;</em><code>nums[0] | nums[1] | ... | nums[n - 1]</code>&nbsp;的最大值。</p>

<p><code>a | b</code>&nbsp;表示两个整数 <code>a</code>&nbsp;和 <code>b</code>&nbsp;的 <strong>按位或</strong>&nbsp;运算。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [12,9], k = 1
<b>输出：</b>30
<b>解释：</b>如果我们对下标为 1 的元素进行操作，新的数组为 [12,18] 。此时得到最优答案为 12 和 18 的按位或运算的结果，也就是 30 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [8,1,2], k = 2
<b>输出：</b>35
<b>解释：</b>如果我们对下标 0 处的元素进行操作，得到新数组 [32,1,2] 。此时得到最优答案为 32|1|2 = 35 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>1 &lt;= k &lt;= 15</code></li>
</ul>
