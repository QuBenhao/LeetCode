# 3736. 最小操作次数使数组元素相等 III [难度分: 1251.75]

<p>给你一个整数数组 <code>nums</code>。</p>

<p>在一步操作中，你可以将任意单个元素 <code>nums[i]</code> 的值&nbsp;<strong>增加</strong> 1。</p>

<p>返回使数组中的所有元素都&nbsp;<strong>相等&nbsp;</strong>所需的&nbsp;<strong>最小总操作次数&nbsp;</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">nums = [2,1,3]</span></p>

<p><strong>输出:</strong> <span class="example-io">3</span></p>

<p><strong>解释:</strong></p>

<p>使所有元素相等的操作如下:</p>

<ul>
	<li>将 <code>nums[0] = 2</code> 增加 1, 变为 3。</li>
	<li>将 <code>nums[1] = 1</code> 增加 1, 变为 2。</li>
	<li>将 <code>nums[1] = 2</code> 增加 1, 变为 3。</li>
</ul>

<p>现在，<code>nums</code> 中的所有元素都等于 3。最小总操作次数为 <code>3</code>。</p>
</div>

<p><strong class="example">示例 2:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">nums = [4,4,5]</span></p>

<p><strong>输出:</strong> <span class="example-io">2</span></p>

<p><strong>解释:</strong></p>

<p>使所有元素相等的操作如下:</p>

<ul>
	<li>将 <code>nums[0] = 4</code> 增加 1, 变为 5。</li>
	<li>将 <code>nums[1] = 4</code> 增加 1, 变为 5。</li>
</ul>

<p>现在，<code>nums</code> 中的所有元素都等于 5。最小总操作次数为 <code>2</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 100</code></li>
</ul>
