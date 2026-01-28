import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input
from PIL import Image
import os

# ==========================
# CONFIG
# ==========================
IMG_SIZE = 224
MODEL_PATH = "plant_disease_efficientnet.keras"   # ✅ UPDATED

CLASS_INFO = {
    "Healthy": "Leaf shows no visible disease symptoms. Normal color, texture, and structure.",
    "Powdery": "Powdery mildew causes white powder-like fungal growth on leaf surfaces.",
    "Rust": "Rust disease produces reddish-brown spots caused by fungal infection."
}

SAMPLE_DIR = "samples"

# ==========================
# LOAD MODEL
# ==========================
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

# ==========================
# PAGE CONFIG
# ==========================
st.set_page_config(
    page_title="Plant Disease Recognition System",
    page_icon="🍀",
    layout="wide"
)

# ==========================
# HEADER (HERO SECTION)
# ==========================
st.markdown(
    """
    <h1 style='
        text-align: center;
        font-size: 80px;
        font-weight: 800;
        margin-bottom: 10px;
    '>
        🌱 Plant Disease Recognition System 🌱
    </h1>

    <p style='
        text-align: center;
        font-size: 30px;
        font-weight: 500;
        margin-top: 5px;
        margin-bottom: 8px;
    '>
        Image-based plant leaf disease detection using Deep Learning
        (EfficientNet + ImageNet)
    </p>

    <p style='
        text-align: center;
        font-size: 16px;
        max-width: 900px;
        margin: auto;
    '>
        This application is trained on a Plant Disease Recognition Dataset
        consisting of labeled leaf images categorized into <b>three classes</b>.
    </p>

    <hr style='margin-top:20px;'>
    """,
    unsafe_allow_html=True
)

# ==========================
# LAYOUT
# ==========================
left_col, right_col = st.columns([1.5, 1])

# =====================================================
# LEFT COLUMN — SAMPLE IMAGES
# =====================================================
with left_col:
    if os.path.exists(SAMPLE_DIR):
        for cls in CLASS_INFO.keys():
            st.markdown(f"#### {cls}")
            class_path = os.path.join(SAMPLE_DIR, cls)

            if os.path.exists(class_path):
                images = os.listdir(class_path)
                cols = st.columns(3)
                for i, img_name in enumerate(images[:3]):
                    img = Image.open(os.path.join(class_path, img_name))
                    cols[i % 3].image(img, width=400)
            else:
                st.info(f"Upload sample images for {cls}")
    else:
        st.warning("Sample images folder not found.")

# =====================================================
# RIGHT COLUMN — PREDICTION
# =====================================================
with right_col:

    st.markdown(
        """
        <h2 style="
            font-size: 40px;
            font-weight: 800;
            margin-bottom: 20px;
        ">
            🌿 Plant Disease Prediction
        </h2>
        """,
        unsafe_allow_html=True
    )

    uploaded_file = st.file_uploader(
        "📤 Upload a plant leaf image (JPG / PNG)",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:
        img = Image.open(uploaded_file).convert("RGB")

        # -------- MODEL PREDICTION --------
        img_resized = img.resize((IMG_SIZE, IMG_SIZE))
        img_array = image.img_to_array(img_resized)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)

        with st.spinner("🔍 Analyzing image..."):
            predictions = model.predict(img_array)
            confidence = float(np.max(predictions))
            class_index = int(np.argmax(predictions))

        class_name = list(CLASS_INFO.keys())[class_index]

        # -------- RESULT (BIG, NO HTML) --------
        st.header("🧠 Prediction Result")
        st.subheader(f"Class: {class_name}")
        st.subheader(f"Confidence: {confidence * 100:.2f}%")

        # -------- IMAGE BELOW RESULT --------
        st.image(img, width=700)

    else:
        st.markdown(
            """
            <p style="
                font-size: 30px;
                margin-top: 20px;
            ">
                👆 Upload an image to start prediction.
            </p>
            """,
            unsafe_allow_html=True
        )
