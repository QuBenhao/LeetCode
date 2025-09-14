# 3678. 大于平均值的最小未出现正整数 

<p>给你一个整数数组 <code>nums</code>。</p>

<p>返回 <code>nums</code> 中 <strong>严格大于</strong> <code>nums</code> 中所有元素 <strong>平均值</strong> 的 <strong>最小未出现正整数</strong>。</p>
数组的 <strong>平均值</strong> 定义为数组中所有元素的总和除以元素的数量。

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">nums = [3,5]</span></p>

<p><strong>输出:</strong> <span class="example-io">6</span></p>

<p><strong>解释:</strong></p>

<ul>
	<li><code>nums</code> 的平均值是 <code>(3 + 5) / 2 = 8 / 2 = 4</code> 。</li>
	<li>大于 4 的最小未出现正整数是 6。</li>
</ul>
</div>

<p><strong class="example">示例 2:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">nums = [-1,1,2]</span></p>

<p><strong>输出:</strong> <span class="example-io">3</span></p>

<p><strong>解释:</strong></p>

<ul>
	<li><code>nums</code> 的平均值是 <code>(-1 + 1 + 2) / 3 = 2 / 3 = 0.667</code> 。</li>
	<li>大于 0.667 的最小未出现正整数是 3 。</li>
</ul>
</div>

<p><strong class="example">示例 3:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">nums = [4,-1]</span></p>

<p><strong>输出:</strong> <span class="example-io">2</span></p>

<p><strong>解释:</strong></p>

<ul>
	<li><code>nums</code> 的平均值是 <code>(4 + (-1)) / 2 = 3 / 2 = 1.50</code>。</li>
	<li>大于 1.50 的最小未出现正整数是 2。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>-100 &lt;= nums[i] &lt;= 100</code></li>
</ul>
