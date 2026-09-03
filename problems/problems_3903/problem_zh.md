# 3903. 最小稳定下标 I [难度分: 1234.75]

<p>给你一个长度为 <code>n</code> 的整数数组 <code>nums</code> 和一个整数 <code>k</code>。</p>

<p>对于每个下标 <code>i</code>，定义它的&nbsp;<strong>不稳定值&nbsp;</strong>为 <code>max(nums[0..i]) - min(nums[i..n - 1])</code>。</p>

<p>换句话说：</p>

<ul>
	<li><code>max(nums[0..i])</code> 表示从下标 0 到下标 <code>i</code> 的元素中的<strong>&nbsp;最大值</strong>&nbsp;。</li>
	<li><code>min(nums[i..n - 1])</code> 表示从下标 <code>i</code> 到下标 <code>n - 1</code> 的元素中的&nbsp;<strong>最小值&nbsp;</strong>。</li>
</ul>

<p>如果某个下标 <code>i</code> 的不稳定值<strong>&nbsp;小于等于</strong> <code>k</code>，则称该下标为&nbsp;<strong>稳定下标</strong>&nbsp;。</p>

<p>返回&nbsp;<strong>最小&nbsp;</strong>的稳定下标。如果不存在这样的下标，则返回 <code>-1</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [5,0,1,4], k = 3</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>在下标 0 处：<code>[5]</code> 中的最大值是 5，<code>[5, 0, 1, 4]</code> 中的最小值是 0，因此不稳定值为 <code>5 - 0 = 5</code>。</li>
	<li>在下标 1 处：<code>[5, 0]</code> 中的最大值是 5，<code>[0, 1, 4]</code> 中的最小值是 0，因此不稳定值为 <code>5 - 0 = 5</code>。</li>
	<li>在下标 2 处：<code>[5, 0, 1]</code> 中的最大值是 5，<code>[1, 4]</code> 中的最小值是 1，因此不稳定值为 <code>5 - 1 = 4</code>。</li>
	<li>在下标 3 处：<code>[5, 0, 1, 4]</code> 中的最大值是 5，<code>[4]</code> 中的最小值是 4，因此不稳定值为 <code>5 - 4 = 1</code>。</li>
	<li>这是第一个不稳定值小于等于 <code>k = 3</code> 的下标，因此答案是 3。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [3,2,1], k = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>在下标 0 处，不稳定值为 <code>3 - 1 = 2</code>。</li>
	<li>在下标 1 处，不稳定值为 <code>3 - 1 = 2</code>。</li>
	<li>在下标 2 处，不稳定值为 <code>3 - 1 = 2</code>。</li>
	<li>这些值都不小于等于 <code>k = 1</code>，因此答案是 <code>-1</code>。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [0], k = 0</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>在下标 0 处，不稳定值为 <code>0 - 0 = 0</code>，它小于等于 <code>k = 0</code>。因此答案是 0。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
	<li><code>0 &lt;= k &lt;= 10<sup>9</sup></code></li>
</ul>
