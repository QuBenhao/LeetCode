# 3190. 使所有元素都可以被 3 整除的最少操作数 [难度分: 1139.54]

<p>给你一个整数数组&nbsp;<code>nums</code>&nbsp;。一次操作中，你可以将&nbsp;<code>nums</code>&nbsp;中的&nbsp;<strong>任意</strong>&nbsp;一个元素增加或者减少 1 。</p>

<p>请你返回将 <code>nums</code>&nbsp;中所有元素都可以被 3 整除的 <strong>最少</strong>&nbsp;操作次数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [1,2,3,4]</span></p>

<p><span class="example-io"><b>输出：</b>3</span></p>

<p><strong>解释：</strong></p>

<p>通过以下 3 个操作，数组中的所有元素都可以被 3 整除：</p>

<ul>
	<li>将 1 减少 1 。</li>
	<li>将 2 增加 1 。</li>
	<li>将 4 减少 1 。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>nums = [3,6,9]</span></p>

<p><span class="example-io"><b>输出：</b>0</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 50</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 50</code></li>
</ul>
