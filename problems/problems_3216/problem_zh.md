# 3216. 交换后字典序最小的字符串 [难度分: 1242.82]

<p>给你一个仅由数字组成的字符串 <code>s</code>，在最多交换一次 <strong>相邻 </strong>且具有相同 <strong>奇偶性 </strong>的数字后，返回可以得到的<span data-keyword="lexicographically-smaller-string">字典序最小的字符串</span>。</p>

<p>如果两个数字都是奇数或都是偶数，则它们具有相同的奇偶性。例如，5 和 9、2 和 4 奇偶性相同，而 6 和 9 奇偶性不同。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "45320"</span></p>

<p><strong>输出：</strong> <span class="example-io">"43520"</span></p>

<p><strong>解释：</strong></p>

<p><code>s[1] == '5'</code> 和 <code>s[2] == '3'</code> 都具有相同的奇偶性，交换它们可以得到字典序最小的字符串。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "001"</span></p>

<p><strong>输出：</strong> <span class="example-io">"001"</span></p>

<p><strong>解释：</strong></p>

<p>无需进行交换，因为 <code>s</code> 已经是字典序最小的。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>2 &lt;= s.length &lt;= 100</code></li>
	<li><code>s</code> 仅由数字组成。</li>
</ul>
