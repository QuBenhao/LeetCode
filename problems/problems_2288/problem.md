# 2288. Apply Discount to Prices [Rating: 1577.11]

<p>A <strong>sentence</strong> is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign <code>&#39;$&#39;</code>. A word represents a <strong>price</strong> if it is a sequence of digits preceded by a dollar sign.</p>

<ul>
	<li>For example, <code>&quot;$100&quot;</code>, <code>&quot;$23&quot;</code>, and <code>&quot;$6&quot;</code> represent prices while <code>&quot;100&quot;</code>, <code>&quot;$&quot;</code>, and <code>&quot;$1e5&quot;</code> do not.</li>
</ul>

<p>You are given a string <code>sentence</code> representing a sentence and an integer <code>discount</code>. For each word representing a price, apply a discount of <code>discount%</code> on the price and <strong>update</strong> the word in the sentence. All updated prices should be represented with <strong>exactly two</strong> decimal places.</p>

<p>Return <em>a string representing the modified sentence</em>.</p>

<p>Note that all prices will contain <strong>at most</strong> <code>10</code> digits.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;there are $1 $2 and 5$ candies in the shop&quot;, discount = 50
<strong>Output:</strong> &quot;there are $0.50 $1.00 and 5$ candies in the shop&quot;
<strong>Explanation:</strong> 
The words which represent prices are &quot;$1&quot; and &quot;$2&quot;. 
- A 50% discount on &quot;$1&quot; yields &quot;$0.50&quot;, so &quot;$1&quot; is replaced by &quot;$0.50&quot;.
- A 50% discount on &quot;$2&quot; yields &quot;$1&quot;. Since we need to have exactly 2 decimal places after a price, we replace &quot;$2&quot; with &quot;$1.00&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> sentence = &quot;1 2 $3 4 $5 $6 7 8$ $9 $10$&quot;, discount = 100
<strong>Output:</strong> &quot;1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $10$&quot;
<strong>Explanation:</strong> 
Applying a 100% discount on any price will result in 0.
The words representing prices are &quot;$3&quot;, &quot;$5&quot;, &quot;$6&quot;, and &quot;$9&quot;.
Each of them is replaced by &quot;$0.00&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= sentence.length &lt;= 10<sup>5</sup></code></li>
	<li><code>sentence</code> consists of lowercase English letters, digits, <code>&#39; &#39;</code>, and <code>&#39;$&#39;</code>.</li>
	<li><code>sentence</code> does not have leading or trailing spaces.</li>
	<li>All words in <code>sentence</code> are separated by a single space.</li>
	<li>All prices will be <strong>positive</strong> numbers without leading zeros.</li>
	<li>All prices will have <strong>at most</strong> <code>10</code> digits.</li>
	<li><code>0 &lt;= discount &lt;= 100</code></li>
</ul>
