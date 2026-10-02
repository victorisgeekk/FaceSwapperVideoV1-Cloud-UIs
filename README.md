# FaceSwapperVideoV1 Cloud UIs

This repo contains ready-to-use starter UI wrappers for running the upstream project
`Deci1337/FaceSwapperVideoV1` in common cloud environments:

- Colab notebook
- Hugging Face Space
- Kaggle notebook
- SageMaker deployment scaffold

The goal is to expose the core CLI as a simple web UI without changing the original repo logic.

## Included projects

- `colab/FaceSwapper_Colab.ipynb` — notebook for Google Colab
- `huggingface_space/app.py` — Gradio UI for Hugging Face Spaces
- `huggingface_space/requirements.txt` — deps for HF Space
- `kaggle/FaceSwapper_Kaggle.ipynb` — notebook for Kaggle
- `sagemaker/app.py` — FastAPI / script entrypoint for SageMaker
- `sagemaker/requirements.txt` — runtime deps for SageMaker
- `sagemaker/entrypoint.sh` — container startup script

## Quick idea

Each cloud wrapper follows the same pattern:

1. Clone or copy the upstream model repo
2. Install dependencies
3. Launch a small web UI
4. Let users upload a source face + video and export the result

## Upstream source

- https://github.com/Deci1337/FaceSwapperVideoV1

## Notes

These files are starter scaffolds meant to be adapted to your account credentials, storage paths, and GPU setup.
The full face-swap pipeline still depends on the upstream repository's actual model files and CUDA-capable environment.
