# 640. 求解方程 

<p>求解一个给定的方程，将<code>x</code>以字符串 <code>"x=#value"</code>&nbsp;的形式返回。该方程仅包含 <code>'+'</code> ， <code>'-'</code> 操作，变量&nbsp;<code>x</code>&nbsp;和其对应系数。</p>

<p>如果方程没有解或存在的解不为整数，请返回&nbsp;<code>"No solution"</code>&nbsp;。如果方程有无限解，则返回 <code>“Infinite solutions”</code> 。</p>

<p>题目保证，如果方程中只有一个解，则 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'x'</span></span></font></font> 的值是一个整数。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入:</strong> equation = "x+5-3+x=6+x-2"
<strong>输出:</strong> "x=2"
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> equation = "x=x"
<strong>输出:</strong> "Infinite solutions"
</pre>

<p><strong>示例 3:</strong></p>

<pre>
<strong>输入:</strong> equation = "2x=x"
<strong>输出:</strong> "x=0"
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul>
	<li><code>3 &lt;= equation.length &lt;= 1000</code></li>
	<li><code>equation</code>&nbsp;只有一个&nbsp;<code>'='</code>.&nbsp;</li>
	<li>方程由绝对值在&nbsp;<code>[0, 100]</code>&nbsp; 范围内且无任何前导零的整数和变量 <code>'x'</code>&nbsp;组成。<span style="display:block"><span style="height:0px"><span style="position:absolute">​​​</span></span></span></li>
</ul>
