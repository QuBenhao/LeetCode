# 2616. 最小化数对的最大差值 [难度分: 2155.34]

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>p</code>&nbsp;。请你从&nbsp;<code>nums</code>&nbsp;中找到&nbsp;<code>p</code> 个下标对，每个下标对对应数值取差值，你需要使得这 <code>p</code> 个差值的&nbsp;<strong>最大值</strong>&nbsp;<strong>最小</strong>。同时，你需要确保每个下标在这&nbsp;<code>p</code>&nbsp;个下标对中最多出现一次。</p>

<p>对于一个下标对&nbsp;<code>i</code>&nbsp;和&nbsp;<code>j</code>&nbsp;，这一对的差值为&nbsp;<code>|nums[i] - nums[j]|</code>&nbsp;，其中&nbsp;<code>|x|</code>&nbsp;表示 <code>x</code>&nbsp;的 <strong>绝对值</strong>&nbsp;。</p>

<p>请你返回 <code>p</code>&nbsp;个下标对对应数值 <strong>最大差值</strong>&nbsp;的 <strong>最小值</strong>&nbsp;。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [10,1,2,7,1,3], p = 2
<b>输出：</b>1
<b>解释：</b>第一个下标对选择 1 和 4 ，第二个下标对选择 2 和 5 。
最大差值为 max(|nums[1] - nums[4]|, |nums[2] - nums[5]|) = max(0, 1) = 1 。所以我们返回 1 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [4,2,1,2], p = 1
<b>输出：</b>0
<b>解释：</b>选择下标 1 和 3 构成下标对。差值为 |2 - 2| = 0 ，这是最大差值的最小值。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= p &lt;= (nums.length)/2</code></li>
</ul>
