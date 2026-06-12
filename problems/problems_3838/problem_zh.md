# 3838. 带权单词映射 

<p>给你一个字符串数组 <code>words</code>，其中每个字符串表示一个由小写英文字母组成的单词。</p>

<p>同时给你一个长度为 26 的整数数组 <code>weights</code>，其中 <code>weights[i]</code> 表示第 <code>i</code> 个小写英文字母的权重。</p>

<p>单词的 <strong>权重</strong> 定义为其所有字符权重的 <strong>总和</strong>。</p>

<p>对于每个单词，将其权重对 26 取模，并将结果按字母倒序映射到一个小写英文字母（<code>0 -&gt; 'z', 1 -&gt; 'y', ..., 25 -&gt; 'a'</code>）。</p>

<p>返回一个由所有单词映射后的字符按顺序连接而成的字符串。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">words = ["abcd","def","xyz"], weights = [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]</span></p>

<p><strong>输出：</strong> <span class="example-io">"rij"</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li><code>"abcd"</code> 的权重是 <code>5 + 3 + 12 + 14 = 34</code>。对 26 取模的结果是 <code>34 % 26 = 8</code>，映射为 <code>'r'</code>。</li>
	<li><code>"def"</code> 的权重是 <code>14 + 1 + 2 = 17</code>。对 26 取模的结果是 <code>17 % 26 = 17</code>，映射为 <code>'i'</code>。</li>
	<li><code>"xyz"</code> 的权重是 <code>7 + 7 + 2 = 16</code>。对&nbsp;26 取模的结果是 <code>16 % 26 = 16</code>，映射为 <code>'j'</code>。</li>
</ul>

<p>因此，连接映射字符后形成的字符串是 <code>"rij"</code>。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">words = ["a","b","c"], weights = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]</span></p>

<p><strong>输出：</strong> <span class="example-io">"yyy"</span></p>

<p><strong>解释：</strong></p>

<p>每个单词的权重均为 1。对 26 取模的结果是 <code>1 % 26 = 1</code>，映射为 <code>'y'</code>。</p>

<p>因此，连接映射字符后形成的字符串是 <code>"yyy"</code>。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">words = ["abcd"], weights = [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5]</span></p>

<p><strong>输出：</strong> <span class="example-io">"g"</span></p>

<p><strong>解释：</strong></p>

<p><code>"abcd"</code> 的权重是 <code>7 + 5 + 3 + 4 = 19</code>。对 26 取模的结果是 <code>19 % 26 = 19</code>，映射为 <code>'g'</code>。</p>

<p>因此，连接映射字符后形成的字符串是 <code>"g"</code>。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 10</code></li>
	<li><code>weights.length == 26</code></li>
	<li><code>1 &lt;= weights[i] &lt;= 100</code></li>
	<li><code>words[i]</code> 仅由小写英文字母组成。</li>
</ul>
