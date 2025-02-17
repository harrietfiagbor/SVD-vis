import matplotlib.pyplot as plt
import streamlit as st

def plot_matrix(matrix, title):
    """Plot a matrix with a colorbar."""
    fig, ax = plt.subplots()
    im = ax.imshow(matrix, cmap='viridis')
    plt.colorbar(im)
    ax.set_title(title)
    return fig

def plot_singular_values(S, k):
    """Plot singular values distribution."""
    fig, ax = plt.subplots()
    ax.plot(S[:100], 'b-', label='Singular Values')
    ax.axvline(x=k, color='r', linestyle='--', label=f'k={k}')
    ax.set_title("Singular Values Distribution")
    ax.set_xlabel("Index")
    ax.set_ylabel("Magnitude")
    ax.legend()
    ax.grid(True)
    return fig

def display_compression_stats(gray_image, k):
    """Display compression statistics."""
    total_values = gray_image.shape[0] * gray_image.shape[1]
    compressed_values = k * (gray_image.shape[0] + gray_image.shape[1])
    compression_ratio = (total_values - compressed_values) / total_values * 100
    
    st.markdown(f"""
    ### Compression Analysis
    - Original matrix size: {total_values} values
    - Compressed representation: {compressed_values} values
    - Compression ratio: {compression_ratio:.2f}%
    """) 