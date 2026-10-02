import os
import subprocess
from pathlib import Path

import gradio as gr

REPO_URL = "https://github.com/Deci1337/FaceSwapperVideoV1.git"
REPO_DIR = Path("/workspace/FaceSwapperVideoV1")
OUTPUT_DIR = Path("/tmp/faceswap-output")


def ensure_repo():
    if not REPO_DIR.exists():
        REPO_DIR.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", REPO_URL, str(REPO_DIR)], check=True)

    requirements = REPO_DIR / "requirements.txt"
    if requirements.exists():
        subprocess.run(["pip", "install", "-r", str(requirements)], check=False)

    subprocess.run(["pip", "install", "gradio"], check=False)


def run_swap(video_path: str, face_path: str, quality: str = "high", provider: str = "cuda"):
    ensure_repo()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "result.mp4"

    cmd = [
        "python",
        str(REPO_DIR / "cli.py"),
        "swap",
        "--input",
        str(video_path),
        "--source-face",
        str(face_path),
        "--output",
        str(output_path),
        "--quality",
        quality,
        "--provider",
        provider,
        "--keep-audio",
        "true",
    ]

    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(REPO_DIR))
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr or proc.stdout or "Face swap failed")

    if not output_path.exists():
        raise FileNotFoundError(f"Expected output at {output_path}")

    return str(output_path)


with gr.Blocks(title="FaceSwapperVideoV1") as demo:
    gr.Markdown("# FaceSwapperVideoV1 — Hugging Face Space")
    gr.Markdown("Run a local face swap with a source image and target video.")

    with gr.Row():
        video = gr.Video(label="Target video")
        source_face = gr.Image(type="filepath", label="Source face image")

    with gr.Row():
        quality = gr.Dropdown(["low", "medium", "high"], value="high", label="Quality")
        provider = gr.Dropdown(["cuda", "cpu", "dml"], value="cuda", label="Provider")

    output = gr.Video(label="Output video")
    submit = gr.Button("Run face swap")
    submit.click(run_swap, inputs=[video, source_face, quality, provider], outputs=output)


demo.launch()
