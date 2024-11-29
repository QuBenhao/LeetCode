# 3232. 判断是否可以赢得数字游戏 [难度分: 1163.36]

<p>给你一个 <strong>正整数 </strong>数组 <code>nums</code>。</p>

<p>Alice 和 Bob 正在玩游戏。在游戏中，Alice 可以从 <code>nums</code> 中选择所有个位数 <strong>或</strong> 所有两位数，剩余的数字归 Bob 所有。如果 Alice 所选数字之和 <strong>严格大于 </strong>Bob 的数字之和，则 Alice 获胜。</p>

<p>如果 Alice 能赢得这场游戏，返回 <code>true</code>；否则，返回 <code>false</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,2,3,4,10]</span></p>

<p><strong>输出：</strong><span class="example-io">false</span></p>

<p><strong>解释：</strong></p>

<p>Alice&nbsp;不管选个位数还是两位数都无法赢得比赛。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [1,2,3,4,5,14]</span></p>

<p><strong>输出：</strong><span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<p>Alice&nbsp;选择个位数可以赢得比赛，所选数字之和为 15。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">nums = [5,5,5,25]</span></p>

<p><strong>输出：</strong><span class="example-io">true</span></p>

<p><strong>解释：</strong></p>

<p>Alice&nbsp;选择两位数可以赢得比赛，所选数字之和为 25。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 100</code></li>
	<li><code>1 &lt;= nums[i] &lt;= 99</code></li>
</ul>
