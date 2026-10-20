# 3863. 将一个字符串排序的最小操作次数 [难度分: 1860.00]

<p data-end="244" data-start="156">给你一个由小写英文字母组成的字符串 <code>s</code>。</p>


<p>在一次操作中，你可以选择 <code>s</code> 的任意 <strong><span data-keyword="substring-nonempty">子字符串</span></strong>（但 <strong>不能</strong> 是整个字符串），并将其按 <strong>非降序字母顺序</strong>&nbsp;进行 <strong>排序</strong>。</p>

<p>返回使 <code>s</code> 按 <strong>非降序</strong> 排列所需的 <strong>最小</strong> 操作次数。如果无法做到，则返回 -1。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "dog"</span></p>

<p><strong>输出：</strong> <span class="example-io">1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>将子字符串 <code>"og"</code> 排序为 <code>"go"</code>。</li>
	<li>现在，<code>s = "dgo"</code>，已按升序排列。因此，答案是 1。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "card"</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>将子字符串 <code>"car"</code> 排序为 <code>"acr"</code>，得到 <code>s = "acrd"</code>。</li>
	<li>将子字符串 <code>"rd"</code> 排序为 <code>"dr"</code>，得到 <code>s = "acdr"</code>，已按升序排列。因此，答案是 2。</li>
</ul>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">s = "gf"</span></p>

<p><strong>输出：</strong> <span class="example-io">-1</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>在给定提示下，无法对 <code>s</code> 进行排序。因此，答案是 -1。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> 仅由小写英文字母组成。</li>
</ul>
