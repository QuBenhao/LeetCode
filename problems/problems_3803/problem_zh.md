# 3803. 统计残差前缀 

<p>给你一个仅由小写英文字母组成的字符串 <code>s</code>。</p>

<p>如果字符串 <code>s</code> 的某个&nbsp;<strong>前缀</strong>&nbsp;中<strong>&nbsp;不同字符的数量</strong>&nbsp;等于 <code>len(prefix) % 3</code>，则该前缀被称为<strong>残差前缀</strong>（residue）。</p>

<p>返回字符串 <code>s</code> 中<strong>&nbsp;残差前缀&nbsp;</strong>的数量。</p>

<p>字符串的<strong>&nbsp;前缀&nbsp;</strong>是一个&nbsp;<strong>非空子字符串</strong>，从字符串的开头起始并延伸到任意位置。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "abc"</span></p>

<p><strong>输出:</strong> <span class="example-io">2</span></p>

<p><strong>解释:</strong>​​​​​​​</p>

<ul>
	<li>前缀 <code>"a"</code> 有 1 个不同字符，且长度模 3 为 1，因此它是一个残差前缀。</li>
	<li>前缀 <code>"ab"</code> 有 2 个不同字符，且长度模 3 为 2，因此它是一个残差前缀。</li>
	<li>前缀 <code>"abc"</code> 不满足条件，因此不是残差前缀。</li>
</ul>

<p>因此，答案是 2。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "dd"</span></p>

<p><strong>输出:</strong> <span class="example-io">1</span></p>

<p><strong>解释:</strong>​​​​​​​</p>

<ul>
	<li>前缀 <code>"d"</code> 有 1 个不同字符，且长度模 3 为 1，因此它是一个残差前缀。</li>
	<li>前缀 <code>"dd"</code> 有 1 个不同字符，但长度模 3 为 2，因此它不是残差前缀。</li>
</ul>

<p>因此，答案是 1。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "bob"</span></p>

<p><strong>输出:</strong> <span class="example-io">2</span></p>

<p><strong>解释:</strong></p>

<ul>
	<li>前缀 <code>"b"</code> 有 1 个不同字符，且长度模 3 为 1，因此它是一个残差前缀。</li>
	<li>前缀 <code>"bo"</code> 有 2 个不同字符，且长度模 3 为 2，因此它是一个残差前缀。</li>
	<li>前缀 <code>"bob"</code> 不满足条件。</li>
</ul>

<p>因此，答案是 2。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅包含小写英文字母。</li>
</ul>
