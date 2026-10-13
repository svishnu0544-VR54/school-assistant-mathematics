# Statistics and Probability

## 1. Measures of Central Tendency
- **Mean ($\bar{x}$):** Direct $\frac{\sum f_i x_i}{\sum f_i}$, Assumed Mean $a + \frac{\sum f_i d_i}{N}$.
- **Median:** For grouped data:
  $$\text{Median} = L + \left(\frac{N/2 - CF}{f}\right) \times h$$
- **Mode:** Most frequent observation:
  $$\text{Mode} = L + \left(\frac{f_1 - f_0}{2f_1 - f_0 - f_2}\right) \times h$$
- **Empirical Relationship:** $\text{Mode} \approx 3 \times \text{Median} - 2 \times \text{Mean}$.

## 2. Measures of Dispersion
- Range $= \text{Max} - \text{Min}$.
- Variance ($\sigma^2$): $\frac{1}{N} \sum (x_i - \bar{x})^2 = \frac{\sum x_i^2}{N} - (\bar{x})^2$.
- Standard Deviation ($\sigma$): $\sigma = \sqrt{\text{Variance}}$.
- Coefficient of Variation (CV): $CV = \frac{\sigma}{\bar{x}} \times 100\%$ (lower CV indicates greater consistency).

## 3. Probability & Distributions
- Classical Probability: $P(E) = \frac{n(E)}{n(S)}$.
- Addition Rule: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$.
- Conditional Probability: $P(A|B) = \frac{P(A \cap B)}{P(B)}$.
- Independent Events: $P(A \cap B) = P(A) P(B)$.
- Bayes' Theorem:
  $$P(E_i|A) = \frac{P(E_i) P(A|E_i)}{\sum_{j} P(E_j) P(A|E_j)}$$
- Binomial Distribution: $P(X = k) = \binom{n}{k} p^k q^{n-k}$ where Mean $= np$, Variance $= npq$.
