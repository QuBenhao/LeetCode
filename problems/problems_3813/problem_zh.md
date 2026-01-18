# 3813. 元音辅音得分 

<p>给你一个字符串 <code>s</code>，由小写英文字母、空格和数字组成。</p>

<p>令 <code>v</code> 表示 <code>s</code> 中元音字母的数量，<code>c</code> 表示辅音字母的数量。</p>

<p>元音字母是 <code>'a'</code>、<code>'e'</code>、<code>'i'</code>、<code>'o'</code> 和 <code>'u'</code>，而英文字母表中除元音外的其他字母均视为辅音字母。</p>

<p>字符串 <code>s</code> 的<strong>&nbsp;得分&nbsp;</strong>定义如下：</p>

<ul>
	<li>如果 <code>c &gt; 0</code>，则 <code>score&nbsp;= floor(v / c)</code>，其中 <code>floor</code> 表示<strong>&nbsp;向下取整&nbsp;</strong>到最接近的整数。</li>
	<li>否则，如果 <code>c = 0</code>，则 <code>score&nbsp;= 0</code>。</li>
</ul>

<p>返回一个整数，表示字符串的得分。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "cooear"</span></p>

<p><strong>输出:</strong> <span class="example-io">2</span></p>

<p><strong>解释:</strong></p>

<p>字符串 <code>s = "cooear"</code> 包含 <code>v = 4</code> 个元音字母 <code>('o', 'o', 'e', 'a')</code> 和 <code>c = 2</code> 个辅音字母 <code>('c', 'r')</code>。</p>

<p>得分为 <code>floor(v / c) = floor(4 / 2) = 2</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "axeyizou"</span></p>

<p><strong>输出:</strong> <span class="example-io">1</span></p>

<p><strong>解释:</strong></p>

<p>字符串 <code>s = "axeyizou"</code> 包含 <code>v = 5</code> 个元音字母 <code>('a', 'e', 'i', 'o', 'u')</code> 和 <code>c = 3</code> 个辅音字母 <code>('x', 'y', 'z')</code>。</p>

<p>得分为 <code>floor(v / c) = floor(5 / 3) = 1</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "au 123"</span></p>

<p><strong>输出:</strong> <span class="example-io">0</span></p>

<p><strong>解释:</strong></p>

<p>字符串 <code>s = "au 123"</code> 不包含辅音字母 <code>(c = 0)</code>，因此得分为 0。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由小写英文字母、空格和数字组成。</li>
</ul>
