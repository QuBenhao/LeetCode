# 1352. 最后 K 个数的乘积 [难度分: 1473.71]

<p>设计一个算法，该算法接受一个整数流并检索该流中最后 <code>k</code> 个整数的乘积。</p>

<p>实现&nbsp;<code>ProductOfNumbers</code>&nbsp;类：</p>

<ul>
	<li><code>ProductOfNumbers()</code>&nbsp;用一个空的流初始化对象。</li>
	<li><code>void add(int num)</code>&nbsp;将数字&nbsp;<code>num</code>&nbsp;添加到当前数字列表的最后面。</li>
	<li><code>int getProduct(int k)</code>&nbsp;返回当前数字列表中，最后&nbsp;<code>k</code>&nbsp;个数字的乘积。你可以假设当前列表中始终 <strong>至少</strong> 包含 <code>k</code> 个数字。</li>
</ul>

<p>题目数据保证：任何时候，任一连续数字序列的乘积都在 32 位整数范围内，不会溢出。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>
<strong>输入：</strong>
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

<strong>输出：</strong>
[null,null,null,null,null,null,20,40,0,null,32]

<strong>解释：</strong>
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // 返回 20 。最后 2 个数字的乘积是 5 * 4 = 20
productOfNumbers.getProduct(3); // 返回 40 。最后 3 个数字的乘积是 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // 返回  0 。最后 4 个数字的乘积是 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // 返回 32 。最后 2 个数字的乘积是 4 * 8 = 32 
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>0 &lt;= num&nbsp;&lt;=&nbsp;100</code></li>
	<li><code>1 &lt;= k &lt;= 4 * 10<sup>4</sup></code></li>
	<li><code>add</code> 和 <code>getProduct</code>&nbsp;最多被调用&nbsp;<code>4 * 10<sup>4</sup></code> 次。</li>
	<li>在任何时间点流的乘积都在 32 位整数范围内。</li>
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>您能否 <strong>同时</strong> 将 <code>GetProduct</code> 和 <code>Add</code> 的实现改为 <code>O(1)</code> 时间复杂度，而不是 <code>O(k)</code> 时间复杂度？</p>
