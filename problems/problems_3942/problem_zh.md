# 3942. 排序排列的最少操作数 [难度分: 1854.85]

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code>，其中 <code>nums</code> 是区间 <code>[0..n - 1]</code> 中所有数字的一个<strong>排列</strong>。</p>

<p>你<strong>&nbsp;只能&nbsp;</strong>执行以下操作：</p>

<ul>
	<li><strong>反转&nbsp;</strong>整个数组。</li>
	<li><strong>左旋一位</strong>：将第一个元素移动到数组末尾，其余元素整体向左移动一位。</li>
</ul>

<p>返回将数组按<strong>&nbsp;递增&nbsp;</strong>顺序排序所需的<strong>&nbsp;最少</strong>&nbsp;操作次数。如果仅使用给定操作无法将数组排序，则返回 <code>-1</code>。</p>

<p><strong>排列&nbsp;</strong>是数组中所有元素的一种重新排列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [0,2,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>左旋一位：<code>[2, 1, 0]</code></li>
	<li>反转数组：<code>[0, 1, 2]</code></li>
</ul>

<p>数组在 2 次操作后变为有序，这是最少操作次数。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,0,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>反转数组：<code>[2, 0, 1]</code></li>
	<li>左旋一位：<code>[0, 1, 2]</code></li>
</ul>

<p>数组在 2 次操作后变为有序，这是最少操作次数。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,0,1,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<p>无法将该数组变为 <code>[0, 1, 2, 3]</code>。因此答案为 <code>-1</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= n - 1</code></li>
	<li><code>nums</code> 是从 0 到 <code>n - 1</code> 的整数排列。</li>
</ul>
