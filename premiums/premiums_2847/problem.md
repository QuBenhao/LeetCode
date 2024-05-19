# 2847. Smallest Number With Given Digit Product

<p>Given a <strong>positive</strong> integer <code>n</code>, return <em>a string representing the <strong>smallest positive</strong> integer such that the product of its digits is equal to</em> <code>n</code><em>, or </em><code>&quot;-1&quot;</code><em> if no such number exists</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 105
<strong>Output:</strong> &quot;357&quot;
<strong>Explanation:</strong> 3 * 5 * 7 = 105. It can be shown that 357 is the smallest number with a product of digits equal to 105. So the answer would be &quot;105&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 7
<strong>Output:</strong> &quot;7&quot;
<strong>Explanation:</strong> Since 7 has only one digit, its product of digits would be 7. We will show that 7 is the smallest number with a product of digits equal to 7. Since the product of numbers 1 to 6 is 1 to 6 respectively, so &quot;7&quot; would be the answer.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 44
<strong>Output:</strong> &quot;-1&quot;
<strong>Explanation:</strong> It can be shown that there is no number such that its product of digits is equal to 44. So the answer would be &quot;-1&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>18</sup></code></li>
</ul>
