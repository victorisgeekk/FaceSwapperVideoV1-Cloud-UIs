# FaceSwapperVideoV1 Cloud UIs

Starter cloud wrappers for the upstream project:
https://github.com/Deci1337/FaceSwapperVideoV1

This repo includes a ready-to-use scaffold for:
- Google Colab
- Kaggle
- Hugging Face Space
- SageMaker

## What these files do

Each folder wraps the original CLI (`python cli.py swap ...`) with a small UI or API so users can upload:
- a target video
- a source face image
- optional quality/provider settings

and then receive an output video.

## Included files

- `colab/FaceSwapper_Colab.ipynb`
- `kaggle/FaceSwapper_Kaggle.ipynb`
- `huggingface_space/app.py`
- `huggingface_space/requirements.txt`
- `sagemaker/app.py`
- `sagemaker/requirements.txt`
- `sagemaker/Dockerfile`
- `sagemaker/entrypoint.sh`

## Prerequisites

The actual image processing still depends on the upstream project and a GPU-capable runtime when available.

Recommended environment:
- CUDA-enabled GPU
- Python 3.10
- FFmpeg installed and on PATH
- Internet access for installing dependencies

## Quick start: local CLI path

```bash
git clone https://github.com/Deci1337/FaceSwapperVideoV1.git
cd FaceSwapperVideoV1
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python cli.py --help
```

## Typical run

```bash
python cli.py swap \
  --input video.mp4 \
  --source-face face.jpg \
  --output result.mp4 \
  --quality high \
  --provider cuda \
  --keep-audio true
```

## Notes

These are starter cloud wrappers only. Production deployment may require:
- persistent storage for uploaded files
- GPU-accelerated containers
- private model cache or mounted volumes
- extended timeout settings
