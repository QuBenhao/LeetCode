# 3827. 统计单比特整数 

<p>给你一个整数&nbsp;<code>n</code>。</p>

<p>如果一个整数的二进制表示中所有位都相同，则称其为<strong>&nbsp;单比特数</strong>（<strong>Monobit</strong>）。</p>

<p>返回范围<code>[0, n]</code>（包括两端）内<strong>&nbsp;单比特数&nbsp;</strong>的个数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 1</span></p>

<p><strong>输出：</strong> <span class="example-io">2</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>范围<code>[0, 1]</code>内的整数对应的二进制表示为<code>"0"</code>和<code>"1"</code>。</li>
	<li>每个表示都由相同的位组成，因此答案是2。</li>
</ul>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 4</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<ul>
	<li>范围<code>[0, 4]</code>内的整数对应的二进制表示为<code>"0"</code>、<code>"1"</code>、<code>"10"</code>、<code>"11"</code>和<code>"100"</code>。</li>
	<li>只有<code>0</code>、<code>1</code>和<code>3</code>满足单比特条件。因此答案是3。</li>
</ul>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 1000</code></li>
</ul>
