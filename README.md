# FaceSwapperVideoV1 Cloud UIs

This repo provides ready-to-use starter UI wrappers for the upstream project:
https://github.com/Deci1337/FaceSwapperVideoV1

Included:
- `colab/FaceSwapper_Colab.ipynb` — Google Colab notebook UI
- `kaggle/FaceSwapper_Kaggle.ipynb` — Kaggle notebook UI
- `huggingface_space/app.py` — Gradio app for Hugging Face Space
- `huggingface_space/requirements.txt` — Space dependencies
- `sagemaker/app.py` — FastAPI app for SageMaker
- `sagemaker/requirements.txt` — SageMaker dependencies
- `sagemaker/entrypoint.sh` — container entrypoint

These are starter templates meant to wrap the upstream CLI and model pipeline. They are not a replacement for the original repo; they are convenience frontends for running the underlying face-swap workflow in cloud environments.
