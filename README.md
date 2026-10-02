# FaceSwapperVideoV1 accountIs

# 🚀 Launch on Cloud Platforms

Click any badge below to open the workspace directly in your own account:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/victorisgeekk/FaceSwapperVideoV1-Cloud-UIs/blob/main/colab/FaceSwapper_Colab.ipynb)
[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://raw.githubusercontent.com/victorisgeekk/FaceSwapperVideoV1-Cloud-UIs/main/kaggle/FaceSwapper_Kaggle.ipynb)
[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/new-space?template=victorisgeekk/FaceSwapperVideoV1-Cloud-UIs)
[![AWS SageMaker](https://img.shields.io/badge/AWS-SageMaker-orange?logo=amazon-aws)](https://github.com/victorisgeekk/FaceSwapperVideoV1-Cloud-UIs/tree/main/sagemaker)


# 🎭 FaceSwapperVideoV1 Cloud Deployment Suite

[![GitHub Stars](https://img.shields.io/github/stars/victorisgeekk/FaceSwapperVideoV1-Cloud-UIs?style=social)](https://github.com/victorisgeekk/FaceSwapperVideoV1-Cloud-UIs)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CUDA Accelerated](https://img.shields.io/badge/CUDA-11.8%20%2F%2012.1-green.svg)](https://developer.nvidia.com/cuda-toolkit)

A cross-platform cloud deployment suite for **[Deci1337/FaceSwapperVideoV1](https://github.com/Deci1337/FaceSwapperVideoV1)**. This repository provides pre-configured, validated scripts and notebooks to run high-fidelity video face swapping across **Google Colab**, **Kaggle**, **Hugging Face Spaces**, and **AWS SageMaker**.

---

## ✨ Features

- **🚀 Universal Cloud Support**: Seamless deployment wrappers for Google Colab, Kaggle, Hugging Face, and AWS SageMaker.
- **🌐 Account-Free Cloudflare Tunnels**: Instant `https://*.trycloudflare.com` HTTPS URLs generated automatically via `pycloudflared` without requiring a Cloudflare account.
- **📱 QR Code Auto-Generation**: QR codes printed directly in the notebook/terminal output for effortless mobile browser access.
- **🎯 Multi-Face Target Locking**: Precision targeting using `--target-face-index` (`0`, `1`, `2`...) to lock and swap specific faces in multi-person videos.
- **✨ Enhanced Quality Output**: Integrated `codeformer` and `gfpgan` face enhancement support with customizable fidelity sliders.
- **⚡ T4 GPU Optimized**: Pre-configured CUDA execution providers and thread management for fast rendering.

---

## 📁 Repository Structure

```text
victorisgeekk/FaceSwapperVideoV1-Cloud-UIs/
├── colab/
│   └── FaceSwapper_Colab.ipynb      # Validated Colab Notebook
├── kaggle/
│   └── FaceSwapper_Kaggle.ipynb     # Validated Kaggle Notebook
├── huggingface_space/
│   ├── app.py                       # Hugging Face Space Entrypoint
│   └── requirements.txt             # Space Dependencies
├── sagemaker/
│   ├── FaceSwapper_SageMaker.ipynb  # Interactive SageMaker Studio Notebook
│   └── app.py                       # Headless / Container Script
└── README.md                        # Documentation
