import gradio as gr

# Demo-mode Hugging Face Space app (lightweight)
# This Space does NOT install heavy ML dependencies (torch, insightface, gfpgan, etc.).
# Instead it provides:
#  - a demo explanation in Burmese
#  - links to run the full pipeline in Colab / Kaggle / SageMaker where GPU is available
#  - optional local preview of uploaded files (no processing)

COLAB_NOTEBOOK = "https://colab.research.google.com/github/victorisgeekk/FaceSwapperVideoV1-Cloud-UIs/blob/main/colab/FaceSwapper_Colab.ipynb"
KAGGLE_NOTEBOOK = "https://www.kaggle.com/kernels"  # users should create a kernel and paste the notebook
SAGEMAKER_DOC = "https://github.com/victorisgeekk/FaceSwapperVideoV1-Cloud-UIs/tree/main/sagemaker"

burmese_instructions = """
ဤ Space သည် demo-mode ဖြစ်သည် — ဤနေရာတွင် မကြီးမားသော ML dependency များ (PyTorch, ONNX, GFPGAN, InsightFace) ကို ထည့်မထားပါ။
ရိုးရှင်းစွာ ပြောရလျှင်၊ Face swap ကို ဤ Space အတွင်း GPU ပေါ် run ပြုလုပ်ရန် မဖြစ်နိုင်ပါ။

အလုပ်လုပ်ပုံအတိုချုံး
1) ဒီ Space တွင် ဗီဒီယိုနှင့် source face ကို upload လုပ်နိုင်သည်။
2) "Open in Colab" ကို နှိပ်၍ Colab notebook ဖြင့် upstream repo ကို clone လုပ်ထားသော environment (GPU) တွင် run ပြုလုပ်နိုင်သည်။
3) Kaggle သို့မဟုတ် SageMaker အတွက် link များကို README တွင်သွား၍ အသေးစိတ်လုပ်ဆောင်ပါ။

ကြိုတင်သတိပေးချက်
- Full face-swap ကို run မည်ဆိုလျှင် Colab/GPU စနစ် သို့သွားပါ။
- Hugging Face Spaces ကို GPU (paid) plan ဖြင့် run မိမိတို့၏ image ကို pre-build လုပ်နိုင်သော်လည်း, အများအားဖြင့် heavy ML dependencies များကို အောင်မြင်စွာ install လုပ်ရန် အခက်အခဲရှိတတ်ပါတယ်။
"""

with gr.Blocks(title="FaceSwapperVideoV1 (Demo)") as demo:
    gr.Markdown("# FaceSwapperVideoV1 — Demo Space")
    gr.Markdown(burmese_instructions)

    with gr.Row():
        video = gr.Video(label="Target video (preview only)")
        face = gr.Image(label="Source face (preview only)")

    with gr.Row():
        colab_btn = gr.Button("Open in Colab (run full pipeline)")
        hf_readme_btn = gr.Button("SageMaker / Deploy docs")

    def open_colab():
        return gr.update(value=COLAB_NOTEBOOK)

    def open_docs():
        return gr.update(value=SAGEMAKER_DOC)

    colab_out = gr.Textbox(label="Colab link")
    docs_out = gr.Textbox(label="Docs link")
    colab_btn.click(open_colab, outputs=colab_out)
    hf_readme_btn.click(open_docs, outputs=docs_out)

    gr.Markdown("---")
    gr.Markdown("If you want a runnable UI in the cloud, use the Colab or SageMaker options where GPU and the full dependencies are available.")

if __name__ == '__main__':
    demo.launch()
