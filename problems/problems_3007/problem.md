# 3007. Maximum Number That Sum of the Prices Is Less Than or Equal to K [Rating: 2258.01]

<p>You are given an integer <code>k</code> and an integer <code>x</code>. The price of a number&nbsp;<code>num</code> is calculated by the count of <span data-keyword="set-bit">set bits</span> at positions <code>x</code>, <code>2x</code>, <code>3x</code>, etc., in its binary representation, starting from the least significant bit. The following table contains examples of how price is calculated.</p>

<table border="1">
	<tbody>
		<tr>
			<th>x</th>
			<th>num</th>
			<th>Binary Representation</th>
			<th>Price</th>
		</tr>
		<tr>
			<td>1</td>
			<td>13</td>
			<td><u>0</u><u>0</u><u>0</u><u>0</u><u>0</u><strong><u>1</u></strong><strong><u>1</u></strong><u>0</u><strong><u>1</u></strong></td>
			<td>3</td>
		</tr>
		<tr>
			<td>2</td>
			<td>13</td>
			<td>0<u>0</u>0<u>0</u>0<strong><u>1</u></strong>1<u>0</u>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>233</td>
			<td>0<strong><u>1</u></strong>1<strong><u>1</u></strong>0<strong><u>1</u></strong>0<u>0</u>1</td>
			<td>3</td>
		</tr>
		<tr>
			<td>3</td>
			<td>13</td>
			<td><u>0</u>00<u>0</u>01<strong><u>1</u></strong>01</td>
			<td>1</td>
		</tr>
		<tr>
			<td>3</td>
			<td>362</td>
			<td><strong><u>1</u></strong>01<strong><u>1</u></strong>01<u>0</u>10</td>
			<td>2</td>
		</tr>
	</tbody>
</table>

<p>The&nbsp;<strong>accumulated price</strong>&nbsp;of&nbsp;<code>num</code>&nbsp;is the <b>total</b>&nbsp;price of&nbsp;numbers from <code>1</code> to <code>num</code>. <code>num</code>&nbsp;is considered&nbsp;<strong>cheap</strong>&nbsp;if its accumulated price&nbsp;is less than or equal to <code>k</code>.</p>

<p>Return the <b>greatest</b>&nbsp;cheap number.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">k = 9, x = 1</span></p>

<p><strong>Output:</strong> <span class="example-io">6</span></p>

<p><strong>Explanation:</strong></p>

<p>As shown in the table below, <code>6</code> is the greatest cheap number.</p>

<table border="1">
	<tbody>
		<tr>
			<th>x</th>
			<th>num</th>
			<th>Binary Representation</th>
			<th>Price</th>
			<th>Accumulated Price</th>
		</tr>
		<tr>
			<td>1</td>
			<td>1</td>
			<td><u>0</u><u>0</u><strong><u>1</u></strong></td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>1</td>
			<td>2</td>
			<td><u>0</u><strong><u>1</u></strong><u>0</u></td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>1</td>
			<td>3</td>
			<td><u>0</u><strong><u>1</u></strong><strong><u>1</u></strong></td>
			<td>2</td>
			<td>4</td>
		</tr>
		<tr>
			<td>1</td>
			<td>4</td>
			<td><strong><u>1</u></strong><u>0</u><u>0</u></td>
			<td>1</td>
			<td>5</td>
		</tr>
		<tr>
			<td>1</td>
			<td>5</td>
			<td><strong><u>1</u></strong><u>0</u><strong><u>1</u></strong></td>
			<td>2</td>
			<td>7</td>
		</tr>
		<tr>
			<td>1</td>
			<td>6</td>
			<td><strong><u>1</u></strong><strong><u>1</u></strong><u>0</u></td>
			<td>2</td>
			<td>9</td>
		</tr>
		<tr>
			<td>1</td>
			<td>7</td>
			<td><strong><u>1</u></strong><strong><u>1</u></strong><strong><u>1</u></strong></td>
			<td>3</td>
			<td>12</td>
		</tr>
	</tbody>
</table>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">k = 7, x = 2</span></p>

<p><strong>Output:</strong> <span class="example-io">9</span></p>

<p><strong>Explanation:</strong></p>

<p>As shown in the table below, <code>9</code> is the greatest cheap number.</p>

<table border="1">
	<tbody>
		<tr>
			<th>x</th>
			<th>num</th>
			<th>Binary Representation</th>
			<th>Price</th>
			<th>Accumulated Price</th>
		</tr>
		<tr>
			<td>2</td>
			<td>1</td>
			<td><u>0</u>0<u>0</u>1</td>
			<td>0</td>
			<td>0</td>
		</tr>
		<tr>
			<td>2</td>
			<td>2</td>
			<td><u>0</u>0<strong><u>1</u></strong>0</td>
			<td>1</td>
			<td>1</td>
		</tr>
		<tr>
			<td>2</td>
			<td>3</td>
			<td><u>0</u>0<strong><u>1</u></strong>1</td>
			<td>1</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>4</td>
			<td><u>0</u>1<u>0</u>0</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>5</td>
			<td><u>0</u>1<u>0</u>1</td>
			<td>0</td>
			<td>2</td>
		</tr>
		<tr>
			<td>2</td>
			<td>6</td>
			<td><u>0</u>1<strong><u>1</u></strong>0</td>
			<td>1</td>
			<td>3</td>
		</tr>
		<tr>
			<td>2</td>
			<td>7</td>
			<td><u>0</u>1<strong><u>1</u></strong>1</td>
			<td>1</td>
			<td>4</td>
		</tr>
		<tr>
			<td>2</td>
			<td>8</td>
			<td><strong><u>1</u></strong>0<u>0</u>0</td>
			<td>1</td>
			<td>5</td>
		</tr>
		<tr>
			<td>2</td>
			<td>9</td>
			<td><strong><u>1</u></strong>0<u>0</u>1</td>
			<td>1</td>
			<td>6</td>
		</tr>
		<tr>
			<td>2</td>
			<td>10</td>
			<td><strong><u>1</u></strong>0<strong><u>1</u></strong>0</td>
			<td>2</td>
			<td>8</td>
		</tr>
	</tbody>
</table>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= 10<sup>15</sup></code></li>
	<li><code>1 &lt;= x &lt;= 8</code></li>
</ul>
