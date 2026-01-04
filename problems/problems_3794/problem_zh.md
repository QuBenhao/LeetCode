# 3794. 反转字符串前缀 

<p>给你一个字符串 <code>s</code> 和一个整数 <code>k</code>。</p>

<p>反转 <code>s</code> 的前 <code>k</code> 个字符，并返回结果字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "abcd", k = 2</span></p>

<p><strong>输出:</strong> <span class="example-io">"bacd"</span></p>

<p><strong>解释:</strong></p>

<p>前 <code>k = 2</code> 个字符 <code>"ab"</code> 反转为 <code>"ba"</code>。最终得到的结果字符串为 <code>"bacd"</code>。</p>
</div>

<p><strong class="example">示例 2:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "xyz", k = 3</span></p>

<p><strong>输出:</strong> <span class="example-io">"zyx"</span></p>

<p><strong>解释:</strong></p>

<p>前 <code>k = 3</code> 个字符 <code>"xyz"</code> 反转为 <code>"zyx"</code>。最终得到的结果字符串为 <code>"zyx"</code>。</p>
</div>

<p><strong class="example">示例 3:</strong></p>

<div class="example-block">
<p><strong>输入:</strong> <span class="example-io">s = "hey", k = 1</span></p>

<p><strong>输出:</strong> <span class="example-io">"hey"</span></p>

<p><strong>解释:</strong></p>

<p>前 <code>k = 1</code> 个字符 <code>"h"</code> 在反转后保持不变。最终得到的结果字符串为 <code>"hey"</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
	<li><code>1 &lt;= k &lt;= s.length</code></li>
</ul>
