# 面试题 08.03. 魔术索引 

<p>魔术索引。 在数组<code>A[0...n-1]</code>中，有所谓的魔术索引，满足条件<code>A[i] = i</code>。给定一个有序整数数组，编写一种方法找出魔术索引，若有的话，在数组A中找出一个魔术索引，如果没有，则返回-1。若有多个魔术索引，返回索引值最小的一个。</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong> 输入</strong>：nums = [0, 2, 3, 4, 5]
<strong> 输出</strong>：0
<strong> 说明：</strong>0下标的元素为0
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong> 输入</strong>：nums = [1, 1, 1]
<strong> 输出</strong>：1
</pre>

<p><strong>说明：</strong></p>

<ol>
	<li>nums长度在[1, 1000000]之间</li>
	<li>此题为原书中的 Follow-up，即数组中可能包含重复元素的版本</li>
</ol>
