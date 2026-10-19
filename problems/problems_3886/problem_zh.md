# 3886. 可排序整数求和 [难度分: 1999.27]

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code>。</p>


<p>如果一个整数 <code>k</code> 满足以下条件，则称其为 <strong>可排序整数</strong>：<code>k</code> 是 <code>n</code> 的&nbsp;<strong>因数</strong>，且可以通过依次执行以下操作将 <code>nums</code> 排序为<strong>&nbsp;非递减顺序</strong>：</p>

<ul>
	<li>将 <code>nums</code> 划分为长度为 <code>k</code> 的<strong>&nbsp;连续子数组</strong>。</li>
	<li><strong>独立地对每个子数组进行循环移动</strong>（左移或右移任意次数）。</li>
</ul>

<p>返回所有可能的可排序整数 <code>k</code> 的和。</p>
<strong>子数组</strong>&nbsp;是数组中的一个连续、非空元素序列。

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [3,1,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>对于 <code>n = 3</code>，可能的因数是 1 和 3。</li>
	<li>对于 <code>k = 1</code>：每个子数组都只有一个元素。无法通过移动使数组排序。</li>
	<li>对于 <code>k = 3</code>：单个子数组 <code>[3, 1, 2]</code> 可以通过左移一次得到 <code>[1, 2, 3]</code>，从而将数组排序。</li>
	<li>只有 <code>k = 3</code> 可排序，因此答案是 3。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [7,6,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>对于 <code>n = 3</code>，可能的因数是 1 和 3。</li>
	<li>对于 <code>k = 1</code>：每个子数组都只有一个元素。无法通过移动使数组排序。</li>
	<li>对于 <code>k = 3</code>：单个子数组 <code>[7, 6, 5]</code> 无法通过任何移动排序为非递减顺序。</li>
	<li>没有任何可排序的&nbsp;<code>k</code>，因此答案是 0。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [5,8]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>对于 <code>n = 2</code>，可能的因数是 1 和 2。</li>
	<li>由于 <code>[5, 8]</code> 本身已经有序，每个因数都可排序。</li>
	<li>因此答案是 <code>1 + 2 = 3</code>。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n == nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
