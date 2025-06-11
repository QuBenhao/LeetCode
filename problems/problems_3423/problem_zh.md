# 3423. 循环数组中相邻元素的最大差值 [难度分: 1184.57]

<p>给你一个 <strong>循环</strong>&nbsp;数组&nbsp;<code>nums</code>&nbsp;，请你找出相邻元素之间的&nbsp;<strong>最大</strong>&nbsp;绝对差值。</p>

<p><b>注意：</b>一个循环数组中，第一个元素和最后一个元素是相邻的。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,4]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>由于&nbsp;<code>nums</code>&nbsp;是循环的，<code>nums[0]</code> 和&nbsp;<code>nums[2]</code>&nbsp;是相邻的，它们之间的绝对差值是最大值&nbsp;<code>|4 - 1| = 3</code>&nbsp;。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [-5,-10,-5]</span></p>

<p><span class="example-io"><b>输出：</b>5</span></p>

<p><b>解释：</b></p>

<p>相邻元素&nbsp;<code>nums[0]</code> 和&nbsp;<code>nums[1]</code>&nbsp;之间的绝对差值为最大值&nbsp;<code>|-5 - (-10)| = 5</code>&nbsp;。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>
