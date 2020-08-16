import streamlit as st
from PIL import Image
from keras.models import load_model
import keras.preprocessing
import numpy as np

# creates web application with user interface using streamlit

st.title("Apollo")

uploaded_file = st.file_uploader("Pick a file")
model = load_model("model.h5")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.write(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    image = image.resize((150, 150))
    img_tensor = keras.preprocessing.image.img_to_array(image)
    img_tensor = np.expand_dims(img_tensor, axis=0)         
    img_tensor /= 255.

    pred = model.predict(img_tensor)

    # checks if the classification is a tumor or not
    if pred>=0.5:
        st.write('Your image has been classified. There is no visible tumor in your MRI scan.')
    if pred<0.5:
        st.write('Your image has been classified. Your MRI scan contains a tumor.')
