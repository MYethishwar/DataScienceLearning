import gradio as gr
import inspect
from Functions import FUNCTIONS
from Descriptions import FUNCTION_DESCRIPTIONS_COMPLETE

FUNCTIONS_REQUIRING_TWO_INPUTS = ["gcd", "lcm", "anagrams", "merge_arrays"]

def run_function(func_name, input_value_1, input_value_2):
    func = FUNCTIONS.get(func_name)
    if not func:
        return "❌ Function not found.", "", ""
    
    try:
        value_1 = eval(input_value_1)

        if func_name in FUNCTIONS_REQUIRING_TWO_INPUTS:
            value_2 = eval(input_value_2)
            result = func(value_1, value_2)
        else:
            result = func(value_1)

    except Exception as e:
        result = f"⚠️ Error: {e}"

    code = inspect.getsource(func)
    details = FUNCTION_DESCRIPTIONS_COMPLETE.get(func_name, {})
    description = (
        f"Description: {details.get('description', 'N/A')}\n"
        f"Expected Input: {details.get('input_type', 'N/A')}\n"
        f"Expected Output: {details.get('output_type', 'N/A')}"
    )
    return result, code, description


def update_description(func_name):
    details = FUNCTION_DESCRIPTIONS_COMPLETE.get(func_name, {})
    return (
        f"Description: {details.get('description', 'N/A')}\n"
        f"Expected Input: {details.get('input_type', 'N/A')}\n"
        f"Expected Output: {details.get('output_type', 'N/A')}"
    )


drops = list(FUNCTIONS.keys())
initial = drops[0] if drops else None
initial_description = update_description(initial)


with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.HTML('<h1 style="text-align:center;">Function Finder – Python Logic Hub</h1>')

    with gr.Row():

        with gr.Column(scale=2):

            gr.Markdown("## ⚙️ Function Selection and Input")

            with gr.Row(variant="compact"):

                with gr.Column(scale=1):
                    func_name = gr.Dropdown(
                        label="Select Function Name:",
                        choices=drops,
                        value=initial
                    )

                with gr.Column(scale=0.5):
                    input_value_1 = gr.Textbox(
                        label="Input 1:",
                        placeholder="e.g. 7 or 'hello'"
                    )

                with gr.Column(scale=0.5):
                    input_value_2 = gr.Textbox(
                        label="Input 2:",
                        placeholder="e.g. 15 or 'olleh'"
                    )

            run_button = gr.Button("▶️ Run Function", variant="primary")

            gr.Markdown("---")

            gr.Markdown("## 📝 Description")
            description_display = gr.Textbox(
                value=initial_description,
                interactive=False,
                label="",
                lines=13
            )

        with gr.Column(scale=1.5):

            gr.Markdown("## ✅ Output")
            output = gr.Textbox(
                label="",
                interactive=False,
                lines=5
            )

            gr.Markdown("---")

            gr.Markdown("## 💻 Source Code")
            code_display = gr.Code(
                label="",
                language="python",
                interactive=False
            )

    func_name.change(
        fn=update_description,
        inputs=func_name,
        outputs=description_display
    )

    run_button.click(
        fn=run_function,
        inputs=[func_name, input_value_1, input_value_2],
        outputs=[output, code_display, description_display]
    )

demo.launch()
