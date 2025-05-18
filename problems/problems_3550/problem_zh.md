# 100668. 数位和等于下标的最小下标 

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;。</p>

<p>返回满足 <code>nums[i]</code>&nbsp;的数位和（每一位数字相加求和）等于 <code>i</code>&nbsp;的 <strong>最小</strong>&nbsp;下标&nbsp;<code>i</code> 。</p>

<p>如果不存在满足要求的下标，返回&nbsp;<code>-1</code> 。</p>

<p>&nbsp;</p>

<p><b>示例 1：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,3,2]</span></p>

<p><span class="example-io"><b>输出：</b>2</span></p>

<p><b>解释：</b></p>

<ul>
	<li><code>nums[2] = 2</code>，其数位和等于&nbsp;2 ，与其下标&nbsp;<code>i = 2</code>&nbsp;相等。因此，输出为&nbsp;2 。</li>
</ul>
</div>

<p><b>示例 2：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,10,11]</span></p>

<p><span class="example-io"><b>输出：</b>1</span></p>

<p><b>解释：</b></p>

<ul>
	<li><code>nums[1] = 10</code>，其数位和等于&nbsp;<code>1 + 0 = 1</code>，与其下标 <code>i = 1</code>&nbsp;相等。</li>
	<li><code>nums[2] = 11</code>，其数位和等于是 <code>1 + 1 = 2</code>，与其下标&nbsp;<code>i = 2</code>&nbsp;相等。</li>
	<li>由于下标 1 是满足要求的最小下标，输出为&nbsp;1 。</li>
</ul>
</div>

<p><b>示例 3：</b></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3]</span></p>

<p><span class="example-io"><b>输出：</b>-1</span></p>

<p><b>解释：</b></p>

<ul>
	<li>由于不存在满足要求的下标，输出为&nbsp;-1 。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>
