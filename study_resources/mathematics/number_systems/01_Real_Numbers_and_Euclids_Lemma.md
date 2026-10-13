# Number Systems: Real Numbers, Euclid's Division Lemma & Surds

## 1. Natural Numbers, Integers, and Real Numbers
- **Natural Numbers (N):** $\{1, 2, 3, \dots\}$
- **Whole Numbers (W):** $\{0, 1, 2, 3, \dots\}$
- **Integers (Z):** $\{\dots, -3, -2, -1, 0, 1, 2, 3, \dots\}$
- **Rational Numbers (Q):** Any number that can be expressed as $\frac{p}{q}$ where $p, q \in \mathbb{Z}$ and $q \neq 0$. In decimal form, rationals are terminating or non-terminating recurring.
- **Irrational Numbers (Q'):** Numbers that cannot be expressed as $\frac{p}{q}$. Their decimal expansions are non-terminating and non-recurring (e.g., $\sqrt{2}, \sqrt{3}, \pi, e$).
- **Real Numbers (R):** The union of rational and irrational numbers ($\mathbb{R} = \mathbb{Q} \cup \mathbb{Q}'$).

## 2. Euclid's Division Lemma and Algorithm
- **Lemma:** Given positive integers $a$ and $b$, there exist unique integers $q$ and $r$ satisfying:
  $$a = bq + r, \quad 0 \le r < b$$
- **HCF by Euclid's Algorithm:** Repeat division until remainder $r = 0$. The last non-zero divisor is $\gcd(a, b)$.
- **Fundamental Theorem of Arithmetic:** Every composite number can be expressed (factorised) as a product of primes uniquely, apart from the order in which the prime factors occur.
- **Relationship:** For two positive integers $a$ and $b$:
  $$\text{HCF}(a, b) \times \text{LCM}(a, b) = a \times b$$

## 3. Surds and Radicals
- An irrational number of the form $\sqrt[n]{a}$ where $a$ is a rational number and $n \in \mathbb{N}, n > 1$ is called a **surd of order $n$**.
- **Laws of Surds:**
  - $(\sqrt[n]{a})^n = a$
  - $\sqrt[n]{a} \times \sqrt[n]{b} = \sqrt[n]{ab}$
  - $\frac{\sqrt[n]{a}}{\sqrt[n]{b}} = \sqrt[n]{\frac{a}{b}}$
  - $\sqrt[m]{\sqrt[n]{a}} = \sqrt[mn]{a}$
- **Rationalisation Factor (RF):**
  - RF of $(\sqrt{a} + \sqrt{b})$ is $(\sqrt{a} - \sqrt{b})$ since $(\sqrt{a} + \sqrt{b})(\sqrt{a} - \sqrt{b}) = a - b$.

## 4. Logarithms
- If $a^x = N$ ($a > 0, a \neq 1$), then $x = \log_a N$.
- **Laws:**
  - $\log_a(xy) = \log_a x + \log_a y$
  - $\log_a(x/y) = \log_a x - \log_a y$
  - $\log_a(x^k) = k \log_a x$
  - **Change of Base:** $\log_b a = \frac{\log_c a}{\log_c b}$
  - $\log_a 1 = 0$, $\log_a a = 1$.

## 5. Complex Numbers
- Standard form: $z = x + iy$ where $i = \sqrt{-1}, i^2 = -1, i^3 = -i, i^4 = 1$.
- **Modulus:** $|z| = \sqrt{x^2 + y^2}$.
- **Conjugate:** $\bar{z} = x - iy$. Note that $z \bar{z} = |z|^2$.
- **Polar Form:** $z = r(\cos \theta + i \sin \theta) = r e^{i\theta}$, where $r = |z|$ and $\theta = \arg(z) = \tan^{-1}(y/x)$.
