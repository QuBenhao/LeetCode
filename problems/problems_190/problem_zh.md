# 190. 颠倒二进制位 

<p>颠倒给定的 32 位有符号整数的二进制位。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 43261596</span></p>

<p><span class="example-io"><b>输出：</b>964176192</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>整数</th>
			<th>二进制</th>
		</tr>
		<tr>
			<td>43261596</td>
			<td>00000010100101000001111010011100</td>
		</tr>
		<tr>
			<td>964176192</td>
			<td>00111001011110000010100101000000</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block">
<p><span class="example-io"><b>输入：</b>n = 2147483644</span></p>

<p><span class="example-io"><b>输出：</b>1073741822</span></p>

<p><strong>解释：</strong></p>

<table>
	<tbody>
		<tr>
			<th>整数</th>
			<th>二进制</th>
		</tr>
		<tr>
			<td>2147483644</td>
			<td>01111111111111111111111111111100</td>
		</tr>
		<tr>
			<td>1073741822</td>
			<td>00111111111111111111111111111110</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= n &lt;= 2<sup>31</sup>&nbsp;- 2</code></li>
	<li><code>n</code>&nbsp;为偶数</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶</strong>: 如果多次调用这个函数，你将如何优化你的算法？</p>
