# Binomial Coefficients

[Permutations and Combinations](../backtrack/permutaions_combinations.md)

## **Binomial Coefficient Sum Identities**

### **1. Sum of All Binomial Coefficients**

**Formula**:
$$
\sum_{k=0}^n \binom{n}{k} = 2^n
$$

**Explanation**:

- **Binomial theorem**: Set $` x = 1 `$ in the binomial expansion:
  $`
  (1 + 1)^n = \sum_{k=0}^n \binom{n}{k} 1^k 1^{n-k} = \sum_{k=0}^n \binom{n}{k}.
  `$
  Therefore, the sum is $` 2^n `$.

- **Combinatorial interpretation**: There are $` 2^n `$ ways to choose any number of elements from $` n `$ elements, including choosing none or all of them.

**Example**:

- When $` n = 3 `$:
  $`
  \binom{3}{0} + \binom{3}{1} + \binom{3}{2} + \binom{3}{3} = 1 + 3 + 3 + 1 = 8 = 2^3.
  `$

### **2. Weighted Sum of Binomial Coefficients (Weighted by Subset Size)**

**Formula**:
$$
\sum_{k=0}^n k \binom{n}{k} = n \cdot 2^{n-1}
$$

**Explanation**:

- **Algebraic derivation**: Differentiate the binomial expansion:
  $`
  \frac{d}{dx} \left( (1+x)^n \right) = n(1+x)^{n-1} = \sum_{k=0}^n k \binom{n}{k} x^{k-1}.
  `$
  Multiply both sides by $` x `$, then set $` x = 1 `$ to obtain:
  $`
  \sum_{k=0}^n k \binom{n}{k} = n \cdot 2^{n-1}.
  `$

- **Combinatorial interpretation**: Choose a committee of any size from $` n `$ people, then choose its chair. This can be counted in two ways:
    1. Choose the chair first ($` n `$ choices), then choose any subset of the remaining $` n-1 `$ people as members ($` 2^{n-1} `$ choices).
    2. Choose $` k `$ people first ($` \binom{n}{k} `$ choices), then choose a chair from those $` k `$ people ($` k `$ choices), giving a total of $
       ` \sum_{k=0}^n k \binom{n}{k} `$。

**Example**:

- When $` n = 4 `$:
  $`
  0\binom{4}{0} + 1\binom{4}{1} + 2\binom{4}{2} + 3\binom{4}{3} + 4\binom{4}{4} = 0 + 4 + 12 + 12 + 4 = 32 = 4 \cdot 2^{3}.
  `$

### **3. Sums of Binomial Coefficients with Odd and Even Indices**

**Formula**:
$$
\sum_{k=1}^{\lceil (n-1)/2 \rceil} \binom{n}{2k+1} = \sum_{k=0}^{\lceil (n-1)/2 \rceil} \binom{n}{2k} = 2^{n-1}
$$

This follows from the binomial expansion.

## **Other Common Binomial Coefficient Sum Identities**

1. **Sum of squares**:
   $`
   \sum_{k=0}^n \binom{n}{k}^2 = \binom{2n}{n}.
   `$
   **Explanation**: Choosing $` n `$ elements from $` 2n `$ elements is equivalent to dividing them into two groups of $` n `$ elements, then choosing $` k `$ from the first group and $` n−k `$ from the second.

2. **Alternating sum**:
   $`
   \sum_{k=0}^n (-1)^k \binom{n}{k} = 0 \quad (n \geq 1).
   `$
   **Explanation**: By the binomial theorem, $` (1 - 1)^n = 0 `$.

## **Summary**

| Sum Type | Formula | Main Derivation Method |
|---------------|---------------------------|-----------|
| Sum of all binomial coefficients | $` 2^n `$ | Binomial theorem |
| Sum weighted by subset size | $` n \cdot 2^{n-1} `$ | Differentiation or a combinatorial argument |
| Sum of squares | $` \binom{2n}{n} `$ | Combinatorial identity |
| Alternating sum | $` 0 `$ (when $` n \geq 1 `$) | Substitute a negative value into the binomial expansion |

These identities are widely used in probability, combinatorial optimization, and algorithm analysis, such as counting state transitions in dynamic programming.

