# Matrices and Determinants

## 1. Matrix Operations
- Addition & subtraction defined for matrices of identical dimensions.
- Multiplication: $A_{m \times k} \times B_{k \times n} = C_{m \times n}$.
- Matrix multiplication is associative but generally **non-commutative** ($AB \neq BA$).
- Transpose properties: $(A + B)^T = A^T + B^T$, $(AB)^T = B^T A^T$.
- Symmetric: $A^T = A$; Skew-symmetric: $A^T = -A$ (diagonal elements are all 0).

## 2. Determinants
- For $2 \times 2$: $\begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$.
- Properties:
  - $\det(A^T) = \det(A)$
  - If any two rows or columns are interchanged, determinant changes sign.
  - If any two rows or columns are identical or proportional, determinant is 0.
  - $\det(AB) = \det(A) \det(B)$.
  - For $n \times n$ matrix $A$, $\det(kA) = k^n \det(A)$.

## 3. Adjoint and Inverse
- $A \cdot \text{adj}(A) = \text{adj}(A) \cdot A = |A| I$.
- Matrix Inverse: $A^{-1} = \frac{1}{|A|} \text{adj}(A)$ exists iff $|A| \neq 0$ (non-singular).
- Properties: $(A^{-1})^{-1} = A$, $(AB)^{-1} = B^{-1} A^{-1}$.

## 4. Solving Systems of Equations
- Matrix Method: $AX = B \implies X = A^{-1} B$.
- Cramer's Rule: $x = \frac{\Delta_x}{\Delta}, y = \frac{\Delta_y}{\Delta}, z = \frac{\Delta_z}{\Delta}$ (valid when $\Delta \neq 0$).
