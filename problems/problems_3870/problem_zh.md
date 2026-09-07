# 3870. 统计范围内的逗号 [难度分: 1149.48]

<p>给你一个整数 <code>n</code>。</p>

<p>返回将所有从 <code>[1, n]</code>（包含两端）范围内的整数以&nbsp;<strong>标准&nbsp;</strong>数字格式书写时所用到的<strong>&nbsp;逗号总数</strong>。</p>

<p>在<strong>&nbsp;标准&nbsp;</strong>格式中：</p>

<ul>
	<li>从右边开始，每&nbsp;<strong>三位&nbsp;</strong>数字后插入一个逗号。</li>
	<li>位数&nbsp;<strong>少于四位&nbsp;</strong>的数字不包含逗号。</li>
</ul>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 1002</span></p>

<p><strong>输出：</strong> <span class="example-io">3</span></p>

<p><strong>解释：</strong></p>

<p>数字 <code>"1,000"</code>、<code>"1,001"</code> 和 <code>"1,002"</code> 每个都包含一个逗号，总计 3 个逗号。</p>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><strong>输入：</strong> <span class="example-io">n = 998</span></p>

<p><strong>输出：</strong> <span class="example-io">0</span></p>

<p><strong>解释：</strong></p>

<p>从 1 到 998 的所有数字位数都少于四位，因此没有使用逗号。</p>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
</ul>
