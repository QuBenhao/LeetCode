# 3572. 选择不同 X 值三元组使 Y 值之和最大 

<p>给你两个整数数组 <code>x</code> 和 <code>y</code>，长度均为 <code>n</code>。你必须选择三个&nbsp;<strong>不同&nbsp;</strong>的下标&nbsp;<code>i</code>&nbsp;，<code>j</code> 和 <code>k</code>，满足以下条件：</p>

<ul>
	<li><code>x[i] != x[j]</code></li>
	<li><code>x[j] != x[k]</code></li>
	<li><code>x[k] != x[i]</code></li>
</ul>

<p>你的目标是在满足这些条件下&nbsp;<strong>最大化</strong> <code>y[i] + y[j] + y[k]</code> 的值。返回通过选择这样一组三元组下标所能获得的&nbsp;<strong>最大&nbsp;</strong>可能和。</p>

<p>如果不存在这样的三元组，返回 -1。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">x = [1,2,1,3,2], y = [5,3,4,6,2]</span></p>

<p><strong>输出：</strong><span class="example-io">14</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>选择 <code>i = 0</code>（<code>x[i] = 1</code>，<code>y[i] = 5</code>），<code>j = 1</code>（<code>x[j] = 2</code>，<code>y[j] = 3</code>），<code>k = 3</code>（<code>x[k] = 3</code>，<code>y[k] = 6</code>）。</li>
	<li>选出的三个 <code>x</code> 中的值互不相同。<code>5 + 3 + 6 = 14</code> 是我们能获得的最大值。因此输出为 14。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">x = [1,2,1,2], y = [4,5,6,7]</span></p>

<p><strong>输出：</strong><span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>x</code> 中只有两个不同的值。因此输出为 -1。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>n == x.length == y.length</code></li>
	<li><code>3 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= x[i], y[i] &lt;= 10<sup>6</sup></code></li>
</ul>
