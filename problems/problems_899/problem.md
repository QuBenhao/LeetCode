# 899. Orderly Queue [Rating: 2096.61]

<p>You are given a string <code>s</code> and an integer <code>k</code>. You can choose one of the first <code>k</code> letters of <code>s</code> and append it at the end of the string.</p>

<p>Return <em>the lexicographically smallest string you could have after applying the mentioned step any number of moves</em>.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cba&quot;, k = 1
<strong>Output:</strong> &quot;acb&quot;
<strong>Explanation:</strong> 
In the first move, we move the 1<sup>st</sup> character &#39;c&#39; to the end, obtaining the string &quot;bac&quot;.
In the second move, we move the 1<sup>st</sup> character &#39;b&#39; to the end, obtaining the final result &quot;acb&quot;.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;baaca&quot;, k = 3
<strong>Output:</strong> &quot;aaabc&quot;
<strong>Explanation:</strong> 
In the first move, we move the 1<sup>st</sup> character &#39;b&#39; to the end, obtaining the string &quot;aacab&quot;.
In the second move, we move the 3<sup>rd</sup> character &#39;c&#39; to the end, obtaining the final result &quot;aaabc&quot;.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= k &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of lowercase English letters.</li>
</ul>
