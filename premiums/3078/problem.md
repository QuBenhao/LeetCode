# 3078. Match Alphanumerical Pattern in Matrix I

<p>You are given a 2D integer matrix <code>board</code> and a 2D character matrix <code>pattern</code>. Where <code>0 &lt;= board[r][c] &lt;= 9</code> and each element of <code>pattern</code> is either a digit or a lowercase English letter.</p>

<p>Your task is to find a <span data-keyword="submatrix">submatrix</span> of <code>board</code> that <strong>matches</strong> <code>pattern</code>.</p>

<p>An integer matrix <code>part</code> matches <code>pattern</code> if we can replace cells containing letters in <code>pattern</code> with some digits (each <strong>distinct</strong> letter with a <strong>unique</strong> digit) in such a way that the resulting matrix becomes identical to the integer matrix <code>part</code>. In other words,</p>

<ul>
	<li>The matrices have identical dimensions.</li>
	<li>If <code>pattern[r][c]</code> is a digit, then <code>part[r][c]</code> must be the <strong>same</strong> digit.</li>
	<li>If <code>pattern[r][c]</code> is a letter <code>x</code>:
	<ul>
		<li>For every <code>pattern[i][j] == x</code>, <code>part[i][j]</code> must be the <strong>same</strong> as <code>part[r][c]</code>.</li>
		<li>For every <code>pattern[i][j] != x</code>, <code>part[i][j]</code> must be <strong>different</strong> than <code>part[r][c]</code>.<span style="display: none;"> </span></li>
	</ul>
	</li>
</ul>

<p>Return <em>an array of length </em><code>2</code><em> containing the row number and column number of the upper-left corner of a submatrix of </em><code>board</code><em> which matches </em><code>pattern</code><em>. If there is more than one such submatrix, return the coordinates of the submatrix with the lowest row index, and in case there is still a tie, return the coordinates of the submatrix with the lowest column index. If there are no suitable answers, return</em> <code>[-1, -1]</code>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div style="display:flex; flex-wrap: wrap; align-items: flex-start; gap: 12px;">
<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">1</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">2</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">2</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">2</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">2</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">3</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">2</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">3</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">3</td>
		</tr>
	</tbody>
</table>

<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">a</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">b</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">b</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">b</td>
		</tr>
	</tbody>
</table>
</div>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">board = [[1,2,2],[2,2,3],[2,3,3]], pattern = [&quot;ab&quot;,&quot;bb&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[0,0]</span></p>

<p><strong>Explanation:</strong> If we consider this mapping: <code>&quot;a&quot; -&gt; 1</code> and <code>&quot;b&quot; -&gt; 2</code>; the submatrix with the upper-left corner <code>(0,0)</code> is a match as outlined in the matrix above.</p>

<p>Note that the submatrix with the upper-left corner (1,1) is also a match but since it comes after the other one, we return <code>[0,0]</code>.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div style="display:flex; flex-wrap: wrap; align-items: flex-start; gap: 12px;">
<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">1</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">1</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">2</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">3</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">3</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">4</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">6</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">6</td>
			<td style="padding: 5px 10px; border: 1px solid red; --darkreader-inline-border-top: #b30000; --darkreader-inline-border-right: #b30000; --darkreader-inline-border-bottom: #b30000; --darkreader-inline-border-left: #b30000;">6</td>
		</tr>
	</tbody>
</table>

<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">a</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">b</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">6</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">6</td>
		</tr>
	</tbody>
</table>
</div>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">board = [[1,1,2],[3,3,4],[6,6,6]], pattern = [&quot;ab&quot;,&quot;66&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,1]</span></p>

<p><strong>Explanation:</strong> If we consider this mapping: <code>&quot;a&quot; -&gt; 3</code> and <code>&quot;b&quot; -&gt; 4</code>; the submatrix with the upper-left corner <code>(1,1)</code> is a match as outlined in the matrix above.</p>

<p>Note that since the corresponding values of <code>&quot;a&quot;</code> and <code>&quot;b&quot;</code> must differ, the submatrix with the upper-left corner <code>(1,0)</code> is not a match. Hence, we return <code>[1,1]</code>.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div style="display:flex; flex-wrap: wrap; align-items: flex-start; gap: 12px;">
<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">1</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">2</td>
		</tr>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">2</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">1</td>
		</tr>
	</tbody>
</table>

<table border="1" cellspacing="3" style="border-collapse: separate; text-align: center;">
	<tbody>
		<tr>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">x</td>
			<td style="padding: 5px 10px; border: 1px solid black; --darkreader-inline-border-top: #8c8273; --darkreader-inline-border-right: #8c8273; --darkreader-inline-border-bottom: #8c8273; --darkreader-inline-border-left: #8c8273;">x</td>
		</tr>
	</tbody>
</table>
</div>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">board = [[1,2],[2,1]], pattern = [&quot;xx&quot;]</span></p>

<p><strong>Output:</strong> <span class="example-io">[-1,-1]</span></p>

<p><strong>Explanation:</strong> Since the values of the matched submatrix must be the same, there is no match. Hence, we return <code>[-1,-1]</code>.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= board.length &lt;= 50</code></li>
	<li><code>1 &lt;= board[i].length &lt;= 50</code></li>
	<li><code>0 &lt;= board[i][j] &lt;= 9</code></li>
	<li><code>1 &lt;= pattern.length &lt;= 50</code></li>
	<li><code>1 &lt;= pattern[i].length &lt;= 50</code></li>
	<li><code>pattern[i][j]</code> is either a digit represented as a string or a lowercase English letter.</li>
</ul>
