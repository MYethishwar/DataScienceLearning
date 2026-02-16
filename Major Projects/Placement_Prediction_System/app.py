import gradio as gr
import pickle
import numpy as np
import random

model = pickle.load(open("modelXG.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

def predict_placement(
    iq, cgpa, academic_performance, internship_experience,
    extra_curricular_score, communication_skills, projects_completed
):
    input_data = np.array([[
        iq, cgpa, academic_performance, internship_experience,
        extra_curricular_score, communication_skills, projects_completed
    ]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        return "# **PLACED** 🎉"
    else:
        return "# **NOT PLACED** ❌"

def autofill_random():
    return (
        random.randint(60, 120),          
        round(random.uniform(5.0, 9.5), 2),
        random.randint(4, 9),             
        random.choice([0, 1]),           
        random.randint(3, 9),              
        random.randint(4, 9),             
        random.randint(1, 5)               
    )

with gr.Blocks(title="Placement Predictor") as app:

    gr.Markdown("# 🎓 Placement Predictor")

    with gr.Row():
        with gr.Column(scale=3):
            gr.Markdown("### 📝 Inputs")
            iq = gr.Number(label="IQ", value=75)
            cgpa = gr.Number(label="CGPA", value=7.5)
            academic_performance = gr.Slider(1, 10, value=7, step=1, label="Academic Performance")
            internship_experience = gr.Radio([0, 1], label="Internship (0 = No, 1 = Yes)", value=1)
            extra_curricular_score = gr.Slider(1, 10, value=6, step=1, label="Extra Curricular Score")
            communication_skills = gr.Slider(1, 10, value=7, step=1, label="Communication Skills")
            projects_completed = gr.Slider(1, 5, value=2, step=1, label="Projects Completed")

        with gr.Column(scale=1):
            gr.Markdown("### 🎯 Output")
            output = gr.Markdown("# **Click Predict**")

            gr.Image(value="image.png", show_label=False)

    with gr.Row():
        predict_btn = gr.Button("🔍 Predict", variant="primary")
        random_btn = gr.Button("🎲 Auto-Fill", variant="secondary")

    predict_btn.click(
        predict_placement,
        inputs=[
            iq,
            cgpa,
            academic_performance,
            internship_experience,
            extra_curricular_score,
            communication_skills,
            projects_completed
        ],
        outputs=output
    )

    random_btn.click(
        autofill_random,
        outputs=[
            iq,
            cgpa,
            academic_performance,
            internship_experience,
            extra_curricular_score,
            communication_skills,
            projects_completed
        ]
    )

app.launch(share=True)
