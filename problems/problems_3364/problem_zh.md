# 3364. 最小正和子数组 [难度分: 1300.56]

<p>给你一个整数数组 <code>nums</code> 和 <strong>两个</strong> 整数 <code>l</code> 和 <code>r</code>。你的任务是找到一个长度在 <code>l</code> 和 <code>r</code> 之间（包含）且和大于 0 的 <strong>子数组</strong> 的 <strong>最小</strong> 和。</p>

<p>返回满足条件的子数组的 <strong>最小</strong> 和。如果不存在这样的子数组，则返回 -1。</p>

<p><strong>子数组</strong> 是数组中的一个连续 <b>非空</b> 元素序列。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [3, -2, 1, 4], l = 2, r = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<p>长度在 <code>l = 2</code> 和 <code>r = 3</code> 之间且和大于 0 的子数组有：</p>

<ul>
	<li><code>[3, -2]</code> 和为 1</li>
	<li><code>[1, 4]</code> 和为 5</li>
	<li><code>[3, -2, 1]</code> 和为 2</li>
	<li><code>[-2, 1, 4]</code> 和为 3</li>
</ul>

<p>其中，子数组 <code>[3, -2]</code> 的和为 1，是所有正和中最小的。因此，答案为 1。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [-2, 2, -3, 1], l = 2, r = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<p>不存在长度在 <code>l</code> 和 <code>r</code> 之间且和大于 0 的子数组。因此，答案为 -1。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1, 2, 3, 4], l = 2, r = 4</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>子数组 <code>[1, 2]</code> 的长度为 2，和为&nbsp;3，是所有正和中最小的。因此，答案为 3。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= l &lt;= r &lt;= nums.length</code></li>
	<li><code>-1000 &lt;= nums[i] &lt;= 1000</code></li>
</ul>
