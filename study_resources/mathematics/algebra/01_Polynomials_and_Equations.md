# Algebra: Polynomials, Linear & Quadratic Equations, Binomial Theorem

## 1. Polynomials
- Standard form: $P(x) = a_n x^n + a_{n-1} x^{n-1} + \dots + a_1 x + a_0$.
- **Remainder Theorem:** If $P(x)$ is divided by $(x - a)$, the remainder is $P(a)$.
- **Factor Theorem:** $(x - a)$ is a factor of $P(x)$ if and only if $P(a) = 0$.

## 2. Pair of Linear Equations in Two Variables
- System: $a_1 x + b_1 y + c_1 = 0$ and $a_2 x + b_2 y + c_2 = 0$.
  1. Unique Solution (Consistent, Intersecting lines): $\frac{a_1}{a_2} \neq \frac{b_1}{b_2}$.
  2. Infinitely Many Solutions (Consistent, Dependent, Coincident lines): $\frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}$.
  3. No Solution (Inconsistent, Parallel lines): $\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}$.

## 3. Quadratic Equations
- Standard form: $ax^2 + bx + c = 0$ ($a \neq 0$).
- Roots by quadratic formula:
  $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
- **Discriminant ($D = b^2 - 4ac$):**
  - $D > 0$: Real, distinct roots.
  - $D = 0$: Real and equal roots ($x = -b / 2a$).
  - $D < 0$: Complex conjugate roots.
- **Vieta's Formulas:**
  - $\alpha + \beta = -b/a$
  - $\alpha \beta = c/a$

## 4. Binomial Theorem
- For any positive integer $n$:
  $$(a + b)^n = \sum_{k=0}^n \binom{n}{k} a^{n-k} b^k$$
- General term: $T_{r+1} = \binom{n}{r} a^{n-r} b^r$.
- Total terms = $n + 1$.
- Sum of binomial coefficients: $C_0 + C_1 + \dots + C_n = 2^n$.
