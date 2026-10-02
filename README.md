# FaceSwapperVideoV1 Cloud UIs

This repository provides complete starter wrappers for running the upstream project:
https://github.com/Deci1337/FaceSwapperVideoV1

## Included

- `colab/FaceSwapper_Colab.ipynb` — Google Colab UI notebook
- `kaggle/FaceSwapper_Kaggle.ipynb` — Kaggle notebook runner
- `huggingface_space/app.py` — Hugging Face Space Gradio app
- `huggingface_space/requirements.txt` — Space dependencies
- `sagemaker/app.py` — FastAPI service
- `sagemaker/requirements.txt` — SageMaker runtime deps
- `sagemaker/Dockerfile` — container image definition
- `sagemaker/entrypoint.sh` — startup script

## Purpose

Each project in this repo wraps the original CLI so you can run the face-swap workflow in a cloud environment without modifying the upstream source code.

## Typical flow

1. Clone the upstream repo
2. Install dependencies
3. Launch a UI or API surface
4. Upload a source face image and target video
5. Run `python cli.py swap ...`
6. Save or preview the output video

## Upstream source

- https://github.com/Deci1337/FaceSwapperVideoV1

## Notes

- These are starter templates. GPU availability and environment setup still matter.
- For best results, run on CUDA-capable GPU instances.
- For Hugging Face Spaces and SageMaker, adapt credentials, storage, and runtime accordingly.
