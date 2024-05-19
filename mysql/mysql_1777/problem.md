# 1777. Product's Price for Each Store

<p>Table: <code>Products</code></p>

<pre>
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store       | enum    |
| price       | int     |
+-------------+---------+
In SQL, (product_id, store) is the primary key for this table.
store is a category of type (&#39;store1&#39;, &#39;store2&#39;, &#39;store3&#39;) where each represents the store this product is available at.
price is the price of the product at this store.
</pre>

<p>&nbsp;</p>

<p>Find the price of each product in each store.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Products table:
+-------------+--------+-------+
| product_id  | store  | price |
+-------------+--------+-------+
| 0           | store1 | 95    |
| 0           | store3 | 105   |
| 0           | store2 | 100   |
| 1           | store1 | 70    |
| 1           | store3 | 80    |
+-------------+--------+-------+
<strong>Output:</strong> 
+-------------+--------+--------+--------+
| product_id  | store1 | store2 | store3 |
+-------------+--------+--------+--------+
| 0           | 95     | 100    | 105    |
| 1           | 70     | null   | 80     |
+-------------+--------+--------+--------+
<strong>Explanation:</strong> 
Product 0 price&#39;s are 95 for store1, 100 for store2 and, 105 for store3.
Product 1 price&#39;s are 70 for store1, 80 for store3 and, it&#39;s not sold in store2.
</pre>
