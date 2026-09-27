# 1614. 括号的最大嵌套深度 [难度分: 1322.83]

<p>给定 <strong>有效括号字符串</strong> <code>s</code>，返回 <code>s</code> 的 <strong>嵌套深度</strong>。嵌套深度是嵌套括号的 <strong>最大</strong> 数量。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>s = "(1+(2*3)+((<strong>8</strong>)/4))+1"</p>

<p><strong>输出：</strong>3</p>

<p><strong>解释：</strong>数字 8 在嵌套的 3 层括号中。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong>s = "(1)+((2))+(((<strong>3</strong>)))"</p>

<p><strong>输出：</strong>3</p>

<p><strong>解释：</strong>数字 3 在嵌套的 3 层括号中。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong><span class="example-io">s = "()(())((()()))"</span></p>

<p><strong>输出：</strong><span class="example-io">3</span></p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 由数字 <code>0-9</code> 和字符 <code>'+'</code>、<code>'-'</code>、<code>'*'</code>、<code>'/'</code>、<code>'('</code>、<code>')'</code> 组成</li>
	<li>题目数据保证括号字符串&nbsp;<code>s</code> 是 <strong>有效的括号字符串</strong></li>
</ul>
