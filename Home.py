import streamlit as st
from PIL import Image


st.subheader("Color to Grayscale Converter")

# Create a file uploader component allowing the user to upload a file
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start CAmera"):
    # Start the camera
    camera_image = st.camera_input("camera")

if camera_image:
    # Create a PILLOW image instance
    img = Image.open(camera_image)

    # Convert the instance to a grayscale image
    gray_camera_img = img.convert("L")

    # Display the grayscale image on the webpage
    st.image(gray_camera_img)

st.slider(
          "Amount",
          min_value=10,
          max_value=30,
)

user_choice = st.radio("Amount", options=[10, 20, 30, 40])

if user_choice == 30:
    st.info("You made the right choice!")


# Check if the image exists meaning the user has uploaded a file
if uploaded_image:
    # Open the user uploaded image with PIL
    img = Image.open(uploaded_image)

    # Convert the image to grayscale
    uploaded_gray_img = img.convert("L")

    # Display the grayscale image on the webpage
    st.image(uploaded_gray_img)

