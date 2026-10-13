# Sets, Relations, and Functions

## 1. Set Theory Fundamentals
- **Representation:** Roster form $\{1, 2, 3\}$ and Set-builder form $\{x : x \in \mathbb{N}, x < 4\}$.
- **Subsets:** If every element of $A$ belongs to $B$, then $A \subseteq B$. Total subsets of a finite set with $n$ elements = $2^n$.
- **Power Set:** $P(A)$ is the set of all subsets of $A$. $|P(A)| = 2^n$.
- **Set Operations:**
  - Union: $A \cup B = \{x : x \in A \text{ or } x \in B\}$
  - Intersection: $A \cap B = \{x : x \in A \text{ and } x \in B\}$
  - Difference: $A - B = \{x : x \in A \text{ and } x \notin B\}$
  - Complement: $A' = U - A$
- **De Morgan's Laws:**
  1. $(A \cup B)' = A' \cap B'$
  2. $(A \cap B)' = A' \cup B'$
- **Cardinality Formulas:**
  - $n(A \cup B) = n(A) + n(B) - n(A \cap B)$
  - $n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(B \cap C) - n(A \cap C) + n(A \cap B \cap C)$

## 2. Relations
- **Cartesian Product:** $A \times B = \{(a, b) : a \in A, b \in B\}$. $|A \times B| = mn$.
- Total number of relations from $A$ to $B$ is $2^{mn}$.
- **Equivalence Relation:** A relation $R$ on set $A$ is an equivalence relation iff:
  1. **Reflexive:** $(a, a) \in R, \forall a \in A$.
  2. **Symmetric:** $(a, b) \in R \implies (b, a) \in R$.
  3. **Transitive:** $(a, b) \in R$ and $(b, c) \in R \implies (a, c) \in R$.

## 3. Functions
- A relation $f: A \to B$ is a function if every element of $A$ has a unique image in $B$.
- **Injective (One-to-One):** $f(x_1) = f(x_2) \implies x_1 = x_2$.
- **Surjective (Onto):** $\text{Range}(f) = \text{Codomain}(B)$.
- **Bijective:** Both injective and surjective (invertible).
- **Composition:** $(g \circ f)(x) = g(f(x))$.
