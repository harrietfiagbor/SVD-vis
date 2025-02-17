import streamlit as st
import numpy as np
from PIL import Image
import requests

from src.image_processing import compress_image, normalize_image, get_rank_one_matrices
from src.visualization import plot_matrix, plot_singular_values, display_compression_stats
from src.utils import EXAMPLE_IMAGES, MARKDOWN_TEXTS

st.title("SVD Image Compression: A Visual Journey")
st.markdown(MARKDOWN_TEXTS["introduction"])

# Image source selection
image_source = st.radio("Choose image source", ["Upload your own", "Use example image"])

if image_source == "Upload your own":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
else:
    selected_example = st.selectbox("Select an example image", list(EXAMPLE_IMAGES.keys()))
    response = requests.get(EXAMPLE_IMAGES[selected_example], stream=True)
    if response.status_code == 200:
        image = Image.open(response.raw)
    else:
        st.error("Failed to load example image. Please try uploading your own image instead.")

if 'image' in locals():
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(image, caption="Original Image", use_container_width=True)
    
    # Convert image to grayscale for matrix visualization
    gray_image = np.array(image.convert('L'))
    with col2:
        st.pyplot(plot_matrix(gray_image, "Original Image Matrix (Grayscale)"))
    
    k = st.slider("Number of Singular Values", 1, 100, 10)
    
    # Compress image
    compressed_image = compress_image(image, k)
    compressed_image_normalized = normalize_image(compressed_image)
    compressed_image_pil = Image.fromarray(compressed_image_normalized)
    
    # Show compressed results
    col3, col4 = st.columns(2)
    with col3:
        st.image(compressed_image_pil, caption=f"Compressed Image (k={k})", use_container_width=True)
    
    # Show matrix representation of compressed image
    gray_compressed = np.array(Image.fromarray(compressed_image_normalized).convert('L'))
    with col4:
        st.pyplot(plot_matrix(gray_compressed, f"Compressed Image Matrix (k={k})"))
    
    # Add SVD analysis
    U, S, Vt = np.linalg.svd(gray_image, full_matrices=False)
    
    # Plot singular values
    st.pyplot(plot_singular_values(S, k))
    
    # Display compression statistics
    display_compression_stats(gray_image, k)
    
    st.markdown(MARKDOWN_TEXTS["low_rank_explanation"])
    
    # Show rank-one components
    num_components_to_show = min(4, k)
    rank_ones, cumulative = get_rank_one_matrices(U, S, Vt, num_components_to_show)
    
    st.markdown("### Individual Rank-One Components")
    cols = st.columns(num_components_to_show)
    for i, (rank_one, col) in enumerate(zip(rank_ones, cols)):
        with col:
            st.pyplot(plot_matrix(rank_one, f"Rank {i+1}"))
    
    st.markdown("### Cumulative Reconstruction")
    cols = st.columns(num_components_to_show)
    for i, (cum_matrix, col) in enumerate(zip(cumulative, cols)):
        with col:
            st.pyplot(plot_matrix(normalize_image(cum_matrix), f"Sum of Ranks 1-{i+1}"))
    
    # Add explanation of rank components right after their visualization
    st.markdown(MARKDOWN_TEXTS["rank_components_explanation"])
    
    # Then add the broader intuition explanation
    st.markdown(MARKDOWN_TEXTS["low_rank_explanation"]) 