# 3798. 最大的偶数 

<p>给你一个仅由字符<code>'1'</code>和<code>'2'</code>组成的字符串<code>s</code>。</p>

<p>你可以删除字符串<code>s</code>中的任意数量的字符，但必须保持剩余字符的顺序不变。</p>

<p>返回可以表示<strong>&nbsp;偶数</strong>&nbsp;整数的<strong>&nbsp;最大结果字符串&nbsp;</strong>。如果不存在这样的字符串，则返回空字符串<code>""</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "1112"</span></p>

<p><strong>输出:</strong> <span class="example-io">"1112"</span></p>

<p><strong>解释:</strong></p>

<p>该字符串已经表示了最大的偶数，因此不需要删除任何字符。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "221"</span></p>

<p><strong>输出:</strong> <span class="example-io">"22"</span></p>

<p><strong>解释:</strong></p>

<p>删除<code>'1'</code>后，可以得到最大的偶数，即 22。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "1"</span></p>

<p><strong>输出:</strong> <span class="example-io">""</span></p>

<p><strong>解释:</strong></p>

<p>无法通过删除字符得到偶数。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由字符 <code>'1'</code> 和 <code>'2'</code> 组成。</li>
</ul>
