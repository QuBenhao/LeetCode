# 2431. Maximize Total Tastiness of Purchased Fruits

<p>You are given two non-negative integer arrays <code>price</code> and <code>tastiness</code>, both arrays have the same length <code>n</code>. You are also given two non-negative integers <code>maxAmount</code> and <code>maxCoupons</code>.</p>

<p>For every integer <code>i</code> in range <code>[0, n - 1]</code>:</p>

<ul>
	<li><code>price[i]</code> describes the price of <code>i<sup>th</sup></code> fruit.</li>
	<li><code>tastiness[i]</code> describes the tastiness of <code>i<sup>th</sup></code> fruit.</li>
</ul>

<p>You want to purchase some fruits such that total tastiness is maximized and the total price does not exceed <code>maxAmount</code>.</p>

<p>Additionally, you can use a coupon to purchase fruit for <strong>half of its price</strong> (rounded down to the closest integer). You can use at most <code>maxCoupons</code> of such coupons.</p>

<p>Return <em>the maximum total tastiness that can be purchased</em>.</p>

<p><strong>Note that:</strong></p>

<ul>
	<li>You can purchase each fruit at most once.</li>
	<li>You can use coupons on some fruit at most once.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> price = [10,20,20], tastiness = [5,8,8], maxAmount = 20, maxCoupons = 1
<strong>Output:</strong> 13
<strong>Explanation:</strong> It is possible to make total tastiness 13 in following way:
- Buy first fruit without coupon, so that total price = 0 + 10 and total tastiness = 0 + 5.
- Buy second fruit with coupon, so that total price = 10 + 10 and total tastiness = 5 + 8.
- Do not buy third fruit, so that total price = 20 and total tastiness = 13.
It can be proven that 13 is the maximum total tastiness that can be obtained.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> price = [10,15,7], tastiness = [5,8,20], maxAmount = 10, maxCoupons = 2
<strong>Output:</strong> 28
<strong>Explanation:</strong> It is possible to make total tastiness 20 in following way:
- Do not buy first fruit, so that total price = 0 and total tastiness = 0.
- Buy second fruit with coupon, so that total price = 0 + 7 and total tastiness = 0 + 8.
- Buy third fruit with coupon, so that total price = 7 + 3 and total tastiness = 8 + 20.
It can be proven that 28 is the maximum total tastiness that can be obtained.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == price.length == tastiness.length</code></li>
	<li><code>1 &lt;= n &lt;= 100</code></li>
	<li><code>0 &lt;= price[i], tastiness[i], maxAmount &lt;= 1000</code></li>
	<li><code>0 &lt;= maxCoupons &lt;= 5</code></li>
</ul>
