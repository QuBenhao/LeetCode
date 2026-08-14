# 3702. 按位异或非零的最长子序列 [难度分: 1489.49]

<p>给你一个整数数组 <code>nums</code>。</p>


<p>返回 <code>nums</code> 中 <strong>按位异或</strong>（XOR）计算结果&nbsp;<strong>非零&nbsp;</strong>的&nbsp;<strong>最长子序列&nbsp;</strong>的长度。如果不存在这样的&nbsp;<strong>子序列&nbsp;</strong>，返回 0 。</p>

<p><strong>子序列&nbsp;</strong>是一个&nbsp;<strong>非空&nbsp;</strong>数组，可以通过从原数组中删除一些或不删除任何元素（不改变剩余元素的顺序）派生而来。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>最长子序列之一是 <code>[2, 3]</code>。按位异或计算为 <code>2 XOR 3 = 1</code>，它是非零的。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [2,3,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>最长子序列是 <code>[2, 3, 4]</code>。按位异或计算为 <code>2 XOR 3 XOR 4 = 5</code>，它是非零的。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
