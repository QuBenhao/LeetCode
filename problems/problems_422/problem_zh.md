# 422. 有效的单词方块

<p>给你一个字符串数组 <code>words</code>，如果它能形成一个有效的<strong> 单词方块 </strong>，则返回 <code>true</code> <em>。</em></p>

<p>有效的单词方块是指此由字符串数组组成的文字方块的&nbsp;第 <code>k</code> 行 和&nbsp;第 <code>k</code> 列所显示的字符串完全相同，其中 <code>0 &lt;= k &lt; max(numRows, numColumns)</code> 。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/validsq1-grid.jpg" style="width: 333px; height: 333px;" />
<pre>
<strong>输入:</strong> words = ["abcd","bnrt","crmy","dtye"]
<strong>输出:</strong> true
<strong>解释:</strong>
第 1 行和第 1 列都读作 "abcd"。
第 2 行和第 2 列都读作 "bnrt"。
第 3 行和第 3 列都读作 "crmy"。
第 4 行和第 4 列都读作 "dtye"。
因此，它构成了一个有效的单词方块。
</pre>

<p><strong class="example">示例 2：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/validsq2-grid.jpg" style="width: 333px; height: 333px;" />
<pre>
<strong>输入:</strong> words = ["abcd","bnrt","crm","dt"]
<strong>输出:</strong> true
<strong>解释:</strong>
第 1 行和第 1 列都读作 "abcd"。
第 2 行和第 2 列都读作 "bnrt"。
第 3 行和第 3 列都读作 "crm"。
第 4 行和第 4 列都读作 "dt"。
因此，它构成了一个有效的单词方块。
</pre>

<p><strong class="example">示例 3：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/validsq3-grid.jpg" style="width: 333px; height: 333px;" />
<pre>
<strong>输入:</strong> words = ["ball","area","read","lady"]
<strong>输出:</strong> false
<strong>解释:</strong>
第 3 行读作 "read" 而第 3 列读作 "lead"。
因此，它不构成一个有效的单词方块。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 500</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 500</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成。</li>
</ul>
