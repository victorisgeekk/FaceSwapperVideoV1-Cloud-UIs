{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# FaceSwapperVideoV1 — Colab UI\n",
    "\n",
    "This notebook launches a simple Gradio UI for the upstream FaceSwapperVideoV1 project.\n",
    "It is designed for quick experimentation in Google Colab with GPU support.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "!git clone https://github.com/Deci1337/FaceSwapperVideoV1.git\n",
    "%cd FaceSwapperVideoV1\n",
    "!python -m pip install --upgrade pip\n",
    "!python -m pip install -r requirements.txt\n",
    "!python -m pip install gradio\n",
    "print('Repository installed. Ready for UI launch.')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import gradio as gr\n",
    "from pathlib import Path\n",
    "\n",
    "def run_swap(video, source_face, quality='high', provider='cuda'):\n",
    "    output_dir = Path('/content/output')\n",
    "    output_dir.mkdir(exist_ok=True, parents=True)\n",
    "\n",
    "    video_path = Path('/content/uploaded_video.mp4')\n",
    "    face_path = Path('/content/uploaded_face.png')\n",
    "    video.save(video_path)\n",
    "    source_face.save(face_path)\n",
    "\n",
    "    cmd = [\n",
    "        'python', 'cli.py', 'swap',\n",
    "        '--input', str(video_path),\n",
    "        '--source-face', str(face_path),\n",
    "        '--output', str(output_dir / 'result.mp4'),\n",
    "        '--quality', quality,\n",
    "        '--provider', provider,\n",
    "        '--keep-audio', 'true'\n",
    "    ]\n",
    "    import subprocess\n",
    "    result = subprocess.run(cmd, capture_output=True, text=True)\n",
    "    if result.returncode != 0:\n",
    "        raise RuntimeError(result.stderr or result.stdout or 'Unknown failure')\n",
    "    return str(output_dir / 'result.mp4')\n",
    "\n",
    "with gr.Blocks() as demo:\n",
    "    gr.Markdown('# FaceSwapperVideoV1 — Colab UI')\n",
    "    with gr.Row():\n",
    "        video = gr.Video(label='Input video')\n",
    "        source_face = gr.Image(label='Source face', type='pil')\n",
    "    quality = gr.Dropdown(['low', 'medium', 'high'], value='high', label='Quality')\n",
    "    provider = gr.Dropdown(['cuda', 'cpu', 'dml'], value='cuda', label='Provider')\n",
    "    out = gr.Video(label='Output video')\n",
    "    btn = gr.Button('Run face swap')\n",
    "    btn.click(fn=run_swap, inputs=[video, source_face, quality, provider], outputs=out)\n",
    "\n",
    "demo.launch(debug=True, share=True)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python",
   "version": "3.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
"path":"colab/FaceSwapper_Colab.ipynb"},{