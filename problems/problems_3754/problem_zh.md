# 3754. 连接非零数字并乘以其数字和 I [难度分: 1247.93]

<p>给你一个整数 <code>n</code>。</p>

<p>将 <code>n</code> 中所有的&nbsp;<strong>非零数字&nbsp;</strong>按照它们的原始顺序连接起来，形成一个新的整数 <code>x</code>。如果不存在&nbsp;<strong>非零数字&nbsp;</strong>，则 <code>x = 0</code>。</p>

<p><code>sum</code> 为 <code>x</code> 中所有数字的&nbsp;<strong>数字和&nbsp;</strong>。</p>

<p>返回一个整数，表示 <code>x * sum</code> 的值。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 10203004</span></p>

<p><strong>输出：</strong> <span class="example-io">12340</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>非零数字是 1、2、3 和 4。因此，<code>x = 1234</code>。</li>
	<li>数字和为 <code>sum = 1 + 2 + 3 + 4 = 10</code>。</li>
	<li>因此，答案是 <code>x * sum = 1234 * 10 = 12340</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 1000</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>非零数字是 1，因此 <code>x = 1</code> 且 <code>sum = 1</code>。</li>
	<li>因此，答案是 <code>x * sum = 1 * 1 = 1</code>。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>
