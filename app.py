
import streamlit as st
from PIL import Image

st.title("Verify You Are Not a Robot")

st.write("Select the images with a fruit to verify you're human.")

# Load images
images = {
    "apple": "images/apple.jpg",
    "banana": "images/banana.jpg",
    "car": "images/car.jpg",
    "grapes": "images/grapes.jpg",
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
    if set(selected_images) == {"apple", "banana", "grapes"}:
        st.success("You are human!")
    else:
        st.error("Verification failed. Are you a robot?")
