{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# FaceSwapperVideoV1 — Kaggle UI\n",
    "\n",
    "Starter notebook for running the original FaceSwapperVideoV1 project on Kaggle.\n"
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
    "print('Dependencies installed')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import subprocess\n",
    "from pathlib import Path\n",
    "\n",
    "def run_faceswap(video_path, face_path, output_dir='/kaggle/working/output'):\n",
    "    Path(output_dir).mkdir(exist_ok=True, parents=True)\n",
    "    out = Path(output_dir) / 'result.mp4'\n",
    "    cmd = [\n",
    "        'python', 'cli.py', 'swap',\n",
    "        '--input', str(video_path),\n",
    "        '--source-face', str(face_path),\n",
    "        '--output', str(out),\n",
    "        '--quality', 'high',\n",
    "        '--provider', 'cuda',\n",
    "        '--keep-audio', 'true'\n",
    "    ]\n",
    "    proc = subprocess.run(cmd, capture_output=True, text=True)\n",
    "    if proc.returncode != 0:\n",
    "        print(proc.stdout)\n",
    "        print(proc.stderr)\n",
    "        raise RuntimeError('Face swap failed')\n",
    "    return str(out)\n"
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
"path":"kaggle/FaceSwapper_Kaggle.ipynb"},{