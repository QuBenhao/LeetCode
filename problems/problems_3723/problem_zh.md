# 3723. 数位平方和的最大值 [难度分: 1536.55]

<p>给你两个&nbsp;<strong>正&nbsp;</strong>整数 <code>num</code> 和 <code>sum</code>。</p>


<p>如果一个正整数 <code>n</code> 满足以下两个条件，则称其为 <strong>好整数</strong>&nbsp;：</p>

<ul>
	<li><code>n</code> 的位数 <strong>恰好</strong> 为 <code>num</code>。</li>
	<li><code>n</code> 的各位数字之和 <strong>恰好</strong>&nbsp;为 <code>sum</code>。</li>
</ul>

<p>一个 <strong>好整数</strong>&nbsp;<code>n</code> 的 <strong>分数&nbsp;</strong>定义为 <code>n</code> 的各位数字的平方和。</p>

<p>返回一个 <strong>字符串</strong>&nbsp;，表示能获得 <strong>最大</strong><strong>分数&nbsp;</strong>的<b> </b><strong>好整数</strong>&nbsp;<code>n</code>。如果有多个可能的整数，返回&nbsp;<strong>最大&nbsp;</strong>的那个。如果不存在这样的整数，返回一个空字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">num = 2, sum = 3</span></p>

<p><strong>输出:</strong> <span class="example-io">"30"</span></p>

<p><strong>解释:</strong></p>

<p>有 3 个好整数：12、21 和 30。</p>

<ul>
	<li>12 的分数是 <code>1<sup>2</sup> + 2<sup>2</sup> = 5</code>。</li>
	<li>21 的分数是 <code>2<sup>2</sup> + 1<sup>2</sup> = 5</code>。</li>
	<li>30 的分数是 <code>3<sup>2</sup> + 0<sup>2</sup> = 9</code>。</li>
</ul>

<p>最大分数是 9，由好整数 30 获得。因此，答案是 <code>"30"</code>。</p>
</div>

<p><strong class="example">示例 2:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">num = 2, sum = 17</span></p>

<p><strong>输出:</strong> <span class="example-io">"98"</span></p>

<p><strong>解释:</strong></p>

<p>有两个好整数：89 和 98。</p>

<ul>
	<li>89 的分数是 <code>8<sup>2</sup> + 9<sup>2</sup> = 145</code>。</li>
	<li>98 的分数是 <code>9<sup>2</sup> + 8<sup>2</sup> = 145</code>。</li>
</ul>

<p>最大分数是 145。获得此分数的最大好整数是 98。因此，答案是 <code>"98"</code>。</p>
</div>

<p><strong class="example">示例 3:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">num = 1, sum = 10</span></p>

<p><strong>输出:</strong> <span class="example-io">""</span></p>

<p><strong>解释:</strong></p>

<p>不存在恰好有 1 位数字且各位数字之和为 10 的整数。因此，答案是 <code>""</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>1 &lt;= sum &lt;= 2 * 10<sup>6</sup></code></li>
</ul>
