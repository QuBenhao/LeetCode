# 面试题 16.02. 单词频率 

<p>设计一个方法，找出任意指定单词在一本书中的出现频率。</p>

<p>你的实现应该支持如下操作：</p>

<ul>
	<li><code>WordsFrequency(book)</code>构造函数，参数为字符串数组构成的一本书</li>
	<li><code>get(word)</code>查询指定单词在书中出现的频率</li>
</ul>

<p><strong>示例：</strong></p>

<pre>WordsFrequency wordsFrequency = new WordsFrequency({&quot;i&quot;, &quot;have&quot;, &quot;an&quot;, &quot;apple&quot;, &quot;he&quot;, &quot;have&quot;, &quot;a&quot;, &quot;pen&quot;});
wordsFrequency.get(&quot;you&quot;); //返回0，&quot;you&quot;没有出现过
wordsFrequency.get(&quot;have&quot;); //返回2，&quot;have&quot;出现2次
wordsFrequency.get(&quot;an&quot;); //返回1
wordsFrequency.get(&quot;apple&quot;); //返回1
wordsFrequency.get(&quot;pen&quot;); //返回1
</pre>

<p><strong>提示：</strong></p>

<ul>
	<li><code>book[i]</code>中只包含小写字母</li>
	<li><code>1 &lt;= book.length &lt;= 100000</code></li>
	<li><code>1 &lt;= book[i].length &lt;= 10</code></li>
	<li><code>get</code>函数的调用次数不会超过100000</li>
</ul>
