import gradio as gr
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
MODEL_PATH = "plant_disease_custom_cnn.h5"
SAMPLE_DIR = "samples"

# ==========================
# LOAD MODEL
# ==========================
model = tf.keras.models.load_model(MODEL_PATH)

# ==========================
# LOAD CLASS NAMES (38 classes)
# ==========================
CLASS_NAMES = list(model.class_names) if hasattr(model, "class_names") else sorted(os.listdir(SAMPLE_DIR))

# ==========================
# AUTO GENERATE CLASS INFO
# ==========================
CLASS_INFO = {cls: f"This leaf belongs to class: {cls}" for cls in CLASS_NAMES}

# ==========================
# LOAD SAMPLE IMAGES
# ==========================
def load_samples():
    images = {}
    for cls in CLASS_NAMES:
        class_path = os.path.join(SAMPLE_DIR, cls)
        if os.path.exists(class_path):
            imgs = sorted(os.listdir(class_path))[:3]
            images[cls] = [os.path.join(class_path, img) for img in imgs]
    return images

# ==========================
# PREDICTION FUNCTION
# ==========================
def predict_disease(img):
    if img is None:
        return None, "⚠️ Please upload a leaf image."

    img = img.convert("RGB").resize((IMG_SIZE, IMG_SIZE))
    arr = image.img_to_array(img)
    arr = np.expand_dims(arr, axis=0)
    arr = preprocess_input(arr)

    preds = model.predict(arr, verbose=0)
    idx = np.argmax(preds)
    confidence = preds[0][idx] * 100
    label = CLASS_NAMES[idx]

    result = f"""
### 🧠 Prediction Result
**Class:** `{label}`  
**Confidence:** `{confidence:.2f}%`
📘 **Description:**  
{CLASS_INFO[label]}
"""
    return img, result

# ==========================
# CUSTOM CSS
# ==========================
CUSTOM_CSS = """
.container {
    max-width: 1200px;
    margin: auto;
}
h1 {
    font-size: 50px !important;
    font-weight: 700;
    margin-bottom: 10px;
}
h2 {
    font-size: 25px !important;
    margin-top: 15px;
    margin-bottom: 6px;
}
h3 {
    font-size: 25px !important;
    margin-top: 10px;
}
.gr-gallery img {
    object-fit: contain !important;
    background-color: #f5f5f5;
    padding: 0px;
}
button {
    font-size: 25px !important;
    padding: 5px 9px !important;
}
"""

# ==========================
# UI
# ==========================
with gr.Blocks(title="Plant Disease Recognition System") as demo:

    gr.Markdown(
        """
        <div style="text-align:center;">
            <h1>🌱 Plant Disease Recognition System</h1>
            <p>Upload a leaf image to detect plant disease using Deep Learning</p>
        </div>
        """
    )

    with gr.Row():

        # -------- LEFT: SAMPLE IMAGES --------
        with gr.Column(scale=1.4):
            samples = load_samples()

            for cls in samples:
                gr.Markdown(f"### 🍃 {cls}")
                gr.Gallery(
                    value=samples[cls],
                    columns=3,
                    height=300,
                    object_fit="cover"
                )

        # -------- RIGHT: PREDICTION --------
        with gr.Column(scale=1):

            image_input = gr.Image(
                type="pil",
                label="Upload Leaf Image",
                height=300
            )
            image_display = gr.Image(
                label="Uploaded Image",
                height=50
            )

            predict_btn = gr.Button("🔍 Predict Disease", size="lg")

            result_output = gr.Markdown()

    # ---------------- ACTION ----------------
    predict_btn.click(
        fn=predict_disease,
        inputs=image_input,
        outputs=[image_display, result_output]
    )

# ==========================
# RUN APP
# ==========================
demo.launch(
    theme=gr.themes.Soft(),
    css=CUSTOM_CSS
)
