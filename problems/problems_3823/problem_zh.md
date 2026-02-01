# 3823. 反转一个字符串里的字母后反转特殊字符 

<p>给你一个由小写英文字母和特殊字符组成的字符串 <code>s</code>。</p>

<p>你的任务是 <strong>按顺序</strong> 执行以下操作：</p>

<ul>
	<li><strong>反转</strong><strong>小写字母</strong>，并将它们放回原来字母所占据的位置。</li>
	<li><strong>反转</strong><strong>特殊字符</strong>，并将它们放回原来特殊字符所占据的位置。</li>
</ul>

<p>返回执行反转操作后的结果字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "</span>)ebc#da@f(<span class="example-io">"</span></p>

<p><strong>输出：</strong> <span class="example-io">"</span>(fad@cb#e)<span class="example-io">"</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>字符串中的字母为 <code>['e', 'b', 'c', 'd', 'a', 'f']</code>：
	<ul>
		<li>反转它们得到 <code>['f', 'a', 'd', 'c', 'b', 'e']</code></li>
		<li><code>s</code> 变为 <code>")fad#cb@e("</code></li>
	</ul>
	</li>
	<li>字符串中的特殊字符为 <code>[')', '#', '@', '(']</code>：
	<ul>
		<li>反转它们得到 <code>['(', '@', '#', ')']</code></li>
		<li><code>s</code> 变为 <code><span class="example-io">"</span>(fad@cb#e)<span class="example-io">"</span></code></li>
	</ul>
	</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "z"</span></p>

<p><strong>输出：</strong> <span class="example-io">"z"</span></p>

<p><strong>解释：</strong></p>

<p>字符串仅包含一个字母，反转它不会改变字符串。没有特殊字符。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "!@#$%^&amp;*()"</span></p>

<p><strong>输出：</strong> <span class="example-io">"</span>)(*&amp;^%$#@!<span class="example-io">"</span></p>

<p><strong>解释：</strong></p>

<p>字符串不包含字母。字符串全部由特殊字符组成，因此反转特殊字符即反转整个字符串。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由小写英文字母和 <code>"!@#$%^&amp;*()"</code> 中的特殊字符组成。</li>
</ul>
