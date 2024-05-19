# 2548. Maximum Price to Fill a Bag

<p>You are given a 2D integer array <code>items</code> where <code>items[i] = [price<sub>i</sub>, weight<sub>i</sub>]</code> denotes the price and weight of the <code>i<sup>th</sup></code> item, respectively.</p>

<p>You are also given a <strong>positive</strong> integer <code>capacity</code>.</p>

<p>Each item can be divided into two items with ratios <code>part1</code> and <code>part2</code>, where <code>part1 + part2 == 1</code>.</p>

<ul>
	<li>The weight of the first item is <code>weight<sub>i</sub> * part1</code> and the price of the first item is <code>price<sub>i</sub> * part1</code>.</li>
	<li>Similarly, the weight of the second item is <code>weight<sub>i</sub> * part2</code> and the price of the second item is <code>price<sub>i</sub> * part2</code>.</li>
</ul>

<p>Return <em><strong>the maximum total price</strong> to fill a bag of capacity</em> <code>capacity</code> <em>with given items</em>. If it is impossible to fill a bag return <code>-1</code>. Answers within <code>10<sup>-5</sup></code> of the <strong>actual answer</strong> will be considered accepted.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> items = [[50,1],[10,8]], capacity = 5
<strong>Output:</strong> 55.00000
<strong>Explanation:</strong> 
We divide the 2<sup>nd</sup> item into two parts with part1 = 0.5 and part2 = 0.5.
The price and weight of the 1<sup>st</sup> item are 5, 4. And similarly, the price and the weight of the 2<sup>nd</sup> item are 5, 4.
The array items after operation becomes [[50,1],[5,4],[5,4]]. 
To fill a bag with capacity 5 we take the 1<sup>st</sup> element with a price of 50 and the 2<sup>nd</sup> element with a price of 5.
It can be proved that 55.0 is the maximum total price that we can achieve.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> items = [[100,30]], capacity = 50
<strong>Output:</strong> -1.00000
<strong>Explanation:</strong> It is impossible to fill a bag with the given item.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= items.length &lt;= 10<sup>5</sup></code></li>
	<li><code>items[i].length == 2</code></li>
	<li><code>1 &lt;= price<sub>i</sub>, weight<sub>i</sub> &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= capacity &lt;= 10<sup>9</sup></code></li>
</ul>
