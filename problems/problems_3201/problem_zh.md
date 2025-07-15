# 3201. 找出有效子序列的最大长度 I [难度分: 1663.76]

<p>给你一个整数数组 <code>nums</code>。</p>

<p><code>nums</code> 的子序列 <code>sub</code> 的长度为 <code>x</code> ，如果其满足以下条件，则称其为 <strong>有效子序列</strong>：</p>

<ul>
	<li><code>(sub[0] + sub[1]) % 2 == (sub[1] + sub[2]) % 2 == ... == (sub[x - 2] + sub[x - 1]) % 2</code></li>
</ul>

<p>返回 <code>nums</code> 的 <strong>最长的有效子序列</strong> 的长度。</p>

<p>一个&nbsp;<strong>子序列</strong>&nbsp;指的是从原数组中删除一些元素（也可以不删除任何元素），剩余元素保持原来顺序组成的新数组。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,3,4]</span></p>

<p><strong>输出：</strong> <span class="example-io">4</span></p>

<p><strong>解释：</strong></p>

<p>最长的有效子序列是 <code>[1, 2, 3, 4]</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,2,1,1,2,1,2]</span></p>

<p><strong>输出：</strong> 6</p>

<p><strong>解释：</strong></p>

<p>最长的有效子序列是 <code>[1, 2, 1, 2, 1, 2]</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">nums = [1,3]</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<p>最长的有效子序列是 <code>[1, 3]</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>7</sup></code></li>
</ul>
