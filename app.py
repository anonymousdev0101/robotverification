
import streamlit as st
from PIL import Image

st.title("Verify You Are Not a Robot")

st.write("Select the images with a cat to verify you're human.")

# Load images
images = {
    "cat1": "images/cat1.jpg",
    "cat2": "images/cat2.jpg",
    "dog1": "images/dog1.jpg",
    "cat3": "images/cat3.jpg",
}

# Display images with checkboxes
selected_images = []
for key, path in images.items():
    img = Image.open(path)
    st.image(img, caption=key, use_column_width=True)
    if st.checkbox(f"Select {key}"):
        selected_images.append(key)

# Validate selection
if st.button("Verify"):
    if set(selected_images) == {"cat1", "cat2", "cat3"}:
        st.success("You are human!")
    else:
        st.error("Verification failed. Are you a robot?")
