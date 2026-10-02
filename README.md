# FaceSwapperVideoV1 Cloud UIs

This repository contains starter UI wrappers for running the upstream project
`Deci1337/FaceSwapperVideoV1` in cloud environments.

Included:
- `colab/FaceSwapper_Colab.ipynb` — Google Colab notebook UI
- `kaggle/FaceSwapper_Kaggle.ipynb` — Kaggle notebook UI
- `huggingface_space/app.py` — Gradio-based Hugging Face Space app
- `huggingface_space/requirements.txt` — HF Space dependencies
- `sagemaker/app.py` — FastAPI service for SageMaker
- `sagemaker/requirements.txt` — SageMaker runtime deps
- `sagemaker/entrypoint.sh` — container startup script

The files are intentionally lightweight starter templates for local cloud deployment.
They are designed to wrap the upstream CLI rather than replace it.

Upstream repo:
https://github.com/Deci1337/FaceSwapperVideoV1
