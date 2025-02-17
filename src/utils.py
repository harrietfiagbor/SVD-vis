EXAMPLE_IMAGES = {
    "Mountain Landscape": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?w=800",
    "City Night": "https://images.unsplash.com/photo-1477959858617-67f85cf4f1df?w=800",
    "Beach Sunset": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=800"
}

MARKDOWN_TEXTS = {
    "introduction": """
## Understanding Singular Value Decomposition (SVD)

Singular Value Decomposition (SVD) is a fundamental matrix factorization technique that decomposes any matrix into three simpler matrices. 
When applied to images, it becomes a powerful tool for compression and analysis.

### Mathematical Foundation
For any matrix $A \in \mathbb{R}^{m \\times n}$, SVD decomposes it into:

$A = U\Sigma V^T$

where:
- $U \in \mathbb{R}^{m \\times m}$ is an orthogonal matrix containing left singular vectors
- $\Sigma \in \mathbb{R}^{m \\times n}$ is a diagonal matrix containing singular values $\sigma_1 \geq \sigma_2 \geq ... \geq \sigma_r \geq 0$
- $V^T \in \mathbb{R}^{n \\times n}$ is the transpose of an orthogonal matrix containing right singular vectors

### Low-Rank Approximation
The power of SVD lies in its ability to create optimal low-rank approximations. For any rank $k$, the best rank-$k$ approximation is:

$A_k = \sum_{i=1}^k \sigma_i u_i v_i^T$

where:
- $\sigma_i$ is the $i$-th singular value
- $u_i$ is the $i$-th column of $U$
- $v_i$ is the $i$-th column of $V$

This approximation minimizes the Frobenius norm $\|A - A_k\|_F$ among all matrices of rank $k$.

### Why is this powerful?
- Each rank-one term $\sigma_i u_i v_i^T$ represents a fundamental pattern in the data
- Singular values $\sigma_i$ indicate the importance of each pattern
- We can achieve efficient compression by keeping only the $k$ largest singular values
- The error is bounded by the discarded singular values: $\|A - A_k\|_2 = \sigma_{k+1}$

Try adjusting the slider below to see how different values of $k$ affect the reconstruction!
""",

    "rank_components_explanation": """
### Understanding Rank-One Components

What we're seeing above is the decomposition:

$A_k = \sum_{i=1}^k \sigma_i u_i v_i^T$

Each component $\sigma_i u_i v_i^T$ is a rank-one matrix that represents:
- A fundamental pattern in the image
- Weighted by its importance ($\sigma_i$)
- Formed by the outer product of left ($u_i$) and right ($v_i$) singular vectors

The cumulative sum shows how these components build up to form our approximation $A_k$.
""",

    "low_rank_explanation": """
## Building Intuition: The Mathematics Behind the Magic

When we perform SVD on an image matrix $A$, we're essentially:

1. **Finding Principal Directions** ($U$ and $V$):
   - $U$ captures vertical patterns
   - $V$ captures horizontal patterns
   - Together they form a basis for expressing our image

2. **Weighting Patterns** ($\Sigma$):
   - Each singular value $\sigma_i$ tells us how important its corresponding pattern is
   - Larger $\sigma_i$ means that pattern contributes more to the final image
   - The rapid decay of singular values ($\sigma_1 \gg \sigma_2 \gg ...$) enables compression

3. **Optimal Approximation**:
   For any chosen rank $k$, SVD gives us the best possible approximation in terms of:
   - Frobenius norm: $\min_{\\text{rank}(B)=k} \|A - B\|_F$
   - Spectral norm: $\min_{\\text{rank}(B)=k} \|A - B\|_2$

This mathematical optimality explains why we get such good results even with aggressive compression!
"""
} 