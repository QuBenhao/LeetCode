# 2588. 统计美丽子数组数目 [难度分: 1696.89]

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组<code>nums</code>&nbsp;。每次操作中，你可以：</p>

<ul>
	<li>选择两个满足&nbsp;<code>0 &lt;= i, j &lt; nums.length</code>&nbsp;的不同下标&nbsp;<code>i</code>&nbsp;和&nbsp;<code>j</code>&nbsp;。</li>
	<li>选择一个非负整数&nbsp;<code>k</code>&nbsp;，满足 <code>nums[i]</code>&nbsp;和 <code>nums[j]</code>&nbsp;在二进制下的第 <code>k</code>&nbsp;位（下标编号从 <strong>0</strong>&nbsp;开始）是 <code>1</code>&nbsp;。</li>
	<li>将 <code>nums[i]</code>&nbsp;和 <code>nums[j]</code>&nbsp;都减去&nbsp;<code>2<sup>k</sup></code>&nbsp;。</li>
</ul>

<p>如果一个子数组内执行上述操作若干次后，该子数组可以变成一个全为 <code>0</code>&nbsp;的数组，那么我们称它是一个 <strong>美丽</strong>&nbsp;的子数组。</p>

<p>请你返回数组 <code>nums</code>&nbsp;中 <strong>美丽子数组</strong>&nbsp;的数目。</p>

<p>子数组是一个数组中一段连续 <strong>非空</strong>&nbsp;的元素序列。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [4,3,1,2,4]
<b>输出：</b>2
<b>解释：</b>nums 中有 2 个美丽子数组：[4,<em><strong>3,1,2</strong></em>,4] 和 [<em><strong>4,3,1,2,4</strong></em>] 。
- 按照下述步骤，我们可以将子数组 [3,1,2] 中所有元素变成 0 ：
  - 选择 [<em><strong>3</strong></em>, 1, <em><strong>2</strong></em>] 和 k = 1 。将 2 个数字都减去 2<sup>1</sup> ，子数组变成 [1, 1, 0] 。
  - 选择 [<em><strong>1</strong></em>, <em><strong>1</strong></em>, 0] 和 k = 0 。将 2 个数字都减去 2<sup>0</sup> ，子数组变成 [0, 0, 0] 。
- 按照下述步骤，我们可以将子数组 [4,3,1,2,4] 中所有元素变成 0 ：
  - 选择 [<em><strong>4</strong></em>, 3, 1, 2, <em><strong>4</strong></em>] 和 k = 2 。将 2 个数字都减去 2<sup>2</sup> ，子数组变成 [0, 3, 1, 2, 0] 。
  - 选择 [0, <em><strong>3</strong></em>, <em><strong>1</strong></em>, 2, 0] 和 k = 0 。将 2 个数字都减去 2<sup>0</sup> ，子数组变成 [0, 2, 0, 2, 0] 。
  - 选择 [0, <em><strong>2</strong></em>, 0, <em><strong>2</strong></em>, 0] 和 k = 1 。将 2 个数字都减去 2<sup>1</sup> ，子数组变成 [0, 0, 0, 0, 0] 。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1,10,4]
<b>输出：</b>0
<b>解释：</b>nums 中没有任何美丽子数组。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>
