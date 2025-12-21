# 3783. 整数的镜像距离 

<p>给你一个整数 <code>n</code>。</p>

<p>定义它的&nbsp;<strong>镜像距离</strong>&nbsp;为：<code>abs(n - reverse(n))</code>​​​​​​​，其中 <code>reverse(n)</code> 表示将 <code>n</code> 的数字反转后形成的整数。</p>

<p>返回表示 <code>n</code> 的镜像距离的整数。</p>

<p>其中，<code>abs(x)</code> 表示 <code>x</code> 的绝对值。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 25</span></p>

<p><strong>输出：</strong> <span class="example-io">27</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>reverse(25) = 52</code>。</li>
	<li>因此，答案为 <code>abs(25 - 52) = 27</code>。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 10</span></p>

<p><strong>输出：</strong> <span class="example-io">9</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>reverse(10) = 01</code>，即 1。</li>
	<li>因此，答案为 <code>abs(10 - 1) = 9</code>。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 7</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>reverse(7) = 7</code>。</li>
	<li>因此，答案为 <code>abs(7 - 7) = 0</code>。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>9</sup></code></li>
</ul>
