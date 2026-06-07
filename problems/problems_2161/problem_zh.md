# 2161. 根据给定数字划分数组 [难度分: 1337.61]

<p>给你一个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums</code>&nbsp;和一个整数&nbsp;<code>pivot</code>&nbsp;。请你将&nbsp;<code>nums</code>&nbsp;重新排列，使得以下条件均成立：</p>

<ul>
	<li>所有小于&nbsp;<code>pivot</code>&nbsp;的元素都出现在所有大于&nbsp;<code>pivot</code>&nbsp;的元素&nbsp;<strong>之前</strong>&nbsp;。</li>
	<li>所有等于&nbsp;<code>pivot</code>&nbsp;的元素都出现在小于和大于 <code>pivot</code>&nbsp;的元素 <strong>中间</strong>&nbsp;。</li>
	<li>小于 <code>pivot</code>&nbsp;的元素之间和大于 <code>pivot</code>&nbsp;的元素之间的 <strong>相对顺序</strong>&nbsp;不发生改变。
	<ul>
		<li>更正式的，考虑每一对&nbsp;<code>p<sub>i</sub></code>，<code>p<sub>j</sub></code>&nbsp;，<code>p<sub>i</sub></code>&nbsp;是初始时位置 <code>i</code>&nbsp;元素的新位置，<code>p<sub>j</sub></code>&nbsp;是初始时位置&nbsp;<code>j</code>&nbsp;元素的新位置。如果&nbsp;<code>i &lt; j</code> 且两个元素&nbsp;<strong>都</strong>&nbsp;小于（或大于）<code>pivot</code>，那么&nbsp;<code>p<sub>i</sub> &lt; p<sub>j</sub></code>&nbsp;。</li>
	</ul>
	</li>
</ul>

<p>请你返回重新排列 <code>nums</code>&nbsp;数组后的结果数组。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [9,12,5,10,14,3,10], pivot = 10
<b>输出：</b>[9,5,3,10,10,12,14]
<b>解释：</b>
元素 9 ，5 和 3 小于 pivot ，所以它们在数组的最左边。
元素 12 和 14 大于 pivot ，所以它们在数组的最右边。
小于 pivot 的元素的相对位置和大于 pivot 的元素的相对位置分别为 [9, 5, 3] 和 [12, 14] ，它们在结果数组中的相对顺序需要保留。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [-3,4,3,2], pivot = 2
<b>输出：</b>[-3,2,4,3]
<b>解释：</b>
元素 -3 小于 pivot ，所以在数组的最左边。
元素 4 和 3 大于 pivot ，所以它们在数组的最右边。
小于 pivot 的元素的相对位置和大于 pivot 的元素的相对位置分别为 [-3] 和 [4, 3] ，它们在结果数组中的相对顺序需要保留。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>6</sup> &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
	<li><code>pivot</code>&nbsp;等于&nbsp;<code>nums</code>&nbsp;中的一个元素。</li>
</ul>
