# Understanding Singular Value Decomposition(SVD) through Image Compression

**Try it live: [SVD Visualization App](https://svd-vis.streamlit.app)**

This interactive visualization demonstrates how Singular Value Decomposition (SVD) can be used for image compression. Through this tool, we can build intuition about why SVD is such a powerful technique in linear algebra and its practical applications.

## The Mathematics Behind SVD

At its core, SVD states that any matrix $A \in \mathbb{R}^{m \times n}$ can be decomposed into:

$A = U\Sigma V^T$

where:
- $U \in \mathbb{R}^{m \times m}$ contains left singular vectors
- $\Sigma \in \mathbb{R}^{m \times n}$ contains singular values $\sigma_1 \geq \sigma_2 \geq ... \geq \sigma_r \geq 0$
- $V^T \in \mathbb{R}^{n \times n}$ contains right singular vectors

## Why is this useful for images?

Images are just matrices of pixel values! When we apply SVD to an image:
1. Each singular value ($\sigma_i$) represents the importance of a pattern
2. The corresponding vectors in $U$ and $V$ describe these patterns
3. We can approximate the image using only the k most important patterns:

$A_k = \sum_{i=1}^k \sigma_i u_i v_i^T$

This gives us the best possible rank-k approximation in terms of both:
- Frobenius norm: $\min_{\\text{rank}(B)=k} \|A - B\|_F$
- Spectral norm: $\min_{\\text{rank}(B)=k} \|A - B\|_2$

## Building Intuition

Think of SVD as finding the most efficient way to describe an image:
1. The first singular value/vectors capture the most dominant pattern
2. Each subsequent component adds more detail
3. Small singular values often correspond to fine details or noise

This is why we can often achieve good compression by keeping just a few components!

## Try It Yourself

This tool lets you:
- Upload your own images or use provided examples
- Adjust the number of singular values used
- See the individual rank-one components
- Watch how the image builds up from these components
- Visualize the singular values distribution

## Quick Start
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Implementation Details

The visualization is built with:
- **Streamlit**: For the interactive interface
- **NumPy**: For SVD computation and matrix operations
- **Pillow**: For image processing
- **Matplotlib**: For visualization of matrices and singular values

The code is organized into modular components for image processing, visualization, and UI, making it easy to extend or modify for educational purposes.

---
*This project was created to help build intuition about SVD through interactive visualization. Feel free to use it for learning or teaching linear algebra concepts!*

