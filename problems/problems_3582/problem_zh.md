# 3582. 为视频标题生成标签 

<p>给你一个字符串 <code><font face="monospace">caption</font></code>，表示一个视频的标题。</p>

<p>需要按照以下步骤&nbsp;<strong>按顺序&nbsp;</strong>生成一个视频的&nbsp;<strong>有效标签&nbsp;</strong>：</p>

<ol>
	<li>
	<p>将 <strong>所有单词&nbsp;</strong>组合为单个&nbsp;<strong>驼峰命名字符串</strong> ，并在前面加上 <code>'#'</code>。<strong>驼峰命名字符串&nbsp;</strong>指的是除第一个单词外，其余单词的首字母大写，且每个单词的首字母之后的字符必须是小写。</p>
	</li>
	<li>
	<p><b>移除&nbsp;</b>所有不是英文字母的字符，但<strong> 保留&nbsp;</strong>第一个字符 <code>'#'</code>。</p>
	</li>
	<li>
	<p>将结果&nbsp;<strong>截断&nbsp;</strong>为最多 100 个字符。</p>
	</li>
</ol>

<p>对 <code>caption</code> 执行上述操作后，返回生成的&nbsp;<strong>标签&nbsp;</strong>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">caption = "Leetcode daily streak achieved"</span></p>

<p><strong>输出：</strong> <span class="example-io">"#leetcodeDailyStreakAchieved"</span></p>

<p><strong>解释：</strong></p>

<p>除了 <code>"leetcode"</code> 以外的所有单词的首字母需要大写。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">caption = "can I Go There"</span></p>

<p><strong>输出：</strong> <span class="example-io">"#canIGoThere"</span></p>

<p><strong>解释：</strong></p>

<p>除了 <code>"can"</code> 以外的所有单词的首字母需要大写。</p>
</div>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">caption = "hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"</span></p>

<p><strong>输出：</strong> <span class="example-io">"#hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"</span></p>

<p><strong>解释：</strong></p>

<p>由于第一个单词长度为 101，因此需要从单词末尾截去最后两个字符。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= caption.length &lt;= 150</code></li>
	<li><code>caption</code> 仅由英文字母和 <code>' '</code> 组成。</li>
</ul>
